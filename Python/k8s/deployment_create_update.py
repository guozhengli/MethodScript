#!/usr/env python
# -*- coding:utf8 -*-
__author__ = '李国征'
__email__ = "745292907@qq.com"

import re
import sys
from os import path

import json
import yaml
from six import iteritems
from kubernetes import client, config, utils
from kubernetes.client import rest


class MyKubernetesApi(object):
    """
    k8s
    功能顺序: 状态-创建-更新-删除-回滚-所有
    """

    def __init__(self):
        config.load_kube_config(config_file="admin-role.yaml")
        self.v1 = client.CoreV1Api()
        self.k8s_client = client.ApiClient()

    # 公共功能

    def from_json_to_yaml(self, json_str):
        """
        将json转换为yaml格式
        :param json_str:
        :return:
        """
        pass

    def create_from_yaml(self, yaml_file, verbose=False, **kwargs):
        """
        根据yaml文件进行创建
        :param yaml_file:
        :param verbose:
        :param kwargs:
        :return:
        """
        k8s_api_list = []
        with open(path.abspath(yaml_file)) as f:
            yml_objects = yaml.load_all(f, Loader=yaml.FullLoader)
            for yml_object in yml_objects:
                group, _, version = yml_object["apiVersion"].partition("/")
                if version == "":
                    version = group
                    group = "core"
                # Take care for the case e.g. api_type is "apiextensions.k8s.io"
                # Only replace the last instance
                group = "".join(group.rsplit(".k8s.io", 1))
                fcn_to_call = "{0}{1}Api".format(group.capitalize(),
                                                 version.capitalize())
                k8s_api = getattr(client, fcn_to_call)(self.k8s_client)
                # Replace CamelCased action_type into snake_case
                kind = yml_object["kind"]
                kind = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', kind)
                kind = re.sub('([a-z0-9])([A-Z])', r'\1_\2', kind).lower()
                # Decide which namespace we are going to put the object in,
                # if any
                if "namespace" in yml_object["metadata"]:
                    namespace = yml_object["metadata"]["namespace"]
                else:
                    namespace = "default"
                # Expect the user to create namespaced objects more often
                try:
                    if hasattr(k8s_api, "create_namespaced_{0}".format(kind)):
                        resp = getattr(k8s_api, "create_namespaced_{0}".format(kind))(
                            body=yml_object, namespace=namespace, **kwargs)
                    else:
                        resp = getattr(k8s_api, "create_{0}".format(kind))(
                            body=yml_object, **kwargs)
                except rest.ApiException as e:
                    k8s_api_list.append("{0} created error!. status='{1}',Reason='{2}'"
                                        .format(kind, str(e.status), str(e.reason)))
                    continue
                if verbose:
                    print("{0} created. status='{1}'".format(kind, str(resp.status)))
                k8s_api_list.append("{0} created. status='{1}'".format(kind, str(resp.status)))
        return k8s_api_list

    def conversion_yaml_to_body(self, yaml_file):
        """
        将yaml格式转换成body方法
        :yaml_file:
        :return:
        """
        k8s_api_list = []
        with open(path.abspath(yaml_file)) as f:
            yml_objects = yaml.load_all(f)
            for yml_object in yml_objects:

                if "namespace" in yml_object["metadata"]:
                    namespace = yml_object["metadata"]["namespace"]
                else:
                    namespace = "default"
                k8s_api_list.append({"namespace":namespace,"body":yml_object})
        return k8s_api_list

    # deployment 相关

    @classmethod
    def get_deployment_status(cls, api_instance, name, namespace="default"):
        """
        获取deployment状态
        :param api_instance:
        :param name:
        :param namespace:
        :return:
        """
        try:
            api_response = api_instance.read_namespaced_deployment_status(
                name=name,
                namespace=namespace,
            )
            return True, api_response
        except rest.ApiException as e:
            return False, "status code:{}, Reason:{}".format(e.status, e.reason)

    @classmethod
    def create_deployment_object(cls, name, labels, selector, replicas=1, volumes=None, containers=None, namespace="default",
                                 resources=None, probe=None):
        """
        实例化 deployment body对象 以传参方式创建deployment
        :param name: str
        :param namespace: str
        :param replicas: int
        :param labes: dict {"project": "www", "app": "java-demo"}
        :param volumes:
        :param containers: list
        :param resources:
        :param livenessProbe:
        :return:
        """

        readiness_probe = liveness_probe = container = ports = volume_mounts = None
        container_list = []

        # 容器挂载磁盘，取决于volumes
        # volume_mounts = [client.V1VolumeMount(name="test-hostpath", mount_path="/tmp")]

        # 端口字典
        # ports = [client.V1ContainerPort(name="web", container_port=80)]

        # 资源控制
        if resources:
            # resources = client.V1ResourceRequirements(
            #     requests={"cpu": "0.5", "memory": "1Gi"},
            #     limits={"cpu": "1", "memory": "2Gi"}
            # )
            resources = client.V1ResourceRequirements(**resources)
        else:
            resources = client.V1ResourceRequirements()

        # 健康检查
        if probe:
            # readiness_probe = liveness_probe = client.V1Probe(
            #     initial_delay_seconds=60,
            #     timeout_seconds=20,
            #     http_get=client.V1HTTPGetAction(port=8014, path="/")
            # )
            http_get = probe.pop("http_get", None)
            probe['http_get'] = client.V1HTTPGetAction(**http_get)
            readiness_probe = liveness_probe = client.V1Probe(**probe)
        # readiness_probe = client.V1Probe(
        #     initial_delay_seconds=60,
        #     timeout_seconds=20,
        #     http_get=client.V1HTTPGetAction(port=8014,  path="/")
        # )

        # 容器字典
        if containers:
            # container = client.V1Container(
            #     name="tomcat",
            #     image="harbor.reapal.com/library/reapal-cloud-web:v1.0.3",
            #     image_pull_policy="Always",
            #     resources=resources,
            #     liveness_probe=liveness_probe,
            #     readiness_probe=readiness_probe,
            #     volume_mounts=volume_mounts,
            #     ports=ports)
            container_list = []
            for container in containers:
                con_ports = container.get("ports", None)
                if con_ports:
                    _tmp_port = []
                    for port in con_ports:
                        _tmp_port.append(client.V1ContainerPort(**port))
                    container['ports'] = _tmp_port

                con_volue_mounts = container.get("volume_mounts", None)
                if con_volue_mounts:
                    _tmp_vms = []
                    for vms in con_volue_mounts:
                        _tmp_vms.append(client.V1VolumeMount(**vms))
                    container["volume_mounts"] = _tmp_vms

                container = client.V1Container(**container)
                container_list.append(container)

        #######
        # 外载磁盘 list
        if volumes:
            # volumes = client.V1Volume(
            #     name="test-hostpath",
            #     host_path=client.V1HostPathVolumeSource(path="/tmp")
            # )
            volumes_host_path = volumes.pop("host_path", None)
            volumes['host_path'] = client.V1HostPathVolumeSource(**volumes_host_path)
            volumes = client.V1Volume(**volumes)

        # spec 模版
        template = client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(labels=labels),
            spec=client.V1PodSpec(
                image_pull_secrets=[client.V1LocalObjectReference(name="k8s-secret")],
                volumes=[volumes],
                containers=container_list
            ))
        if selector:
            # selector = client.V1LabelSelector(
            #     match_labels=labels
            # )

            selector = client.V1LabelSelector(**selector)

        # deployment 载体(spec)
        spec = client.ExtensionsV1beta1DeploymentSpec(
            replicas=replicas,
            selector=selector,
            template=template)

        # 实例化deployment对象
        deployment = client.ExtensionsV1beta1Deployment(
            api_version="extensions/v1beta1",
            kind="Deployment",
            metadata=client.V1ObjectMeta(name=name, namespace=namespace),
            spec=spec)

        return deployment
    @classmethod
    def create_deployment(self, api_instance, deployment_body, namespace="default"):
        """
        创建 deployement 以传yaml-body方式创建
        :param api_instance:
        :param deployment:
        :return:
        """

        api_response = api_instance.create_namespaced_deployment(
            body=deployment_body,
            namespace=namespace)
        return str(api_response.status)

    def update_deployment(self, name, api_instance, deployment, image, replicas=None, namespace="default"):
        """
        进行image更新以及容器容量更新
        :param api_instance:
        :param deployment:
        :param image: str
        :param replicas: 为None时不更新
        :return:
        """
        print('update deployment args -->', name, image, replicas)

        # 更新容器镜像和容器数量
        deployment.spec.template.spec.containers[0].image = image
        if replicas:
            deployment.spec.replicas = replicas

        # 更新depolyment
        try:
            api_response = api_instance.patch_namespaced_deployment(
                name=name,
                namespace=namespace,
                body=deployment)
            return True, api_response.status
        except rest.ApiException as e:
            return False, e

    def delete_deployment(self,name, api_instance, namespace="default"):
        # 删除 deployment
        api_response = api_instance.delete_namespaced_deployment(
            name=name,
            namespace=namespace,
            body=client.V1DeleteOptions(
                propagation_policy='Foreground',
                grace_period_seconds=5))
        return str(api_response.status)

    def rollback_deployment_object(self, deployment_name=""):
        """
        回滚到上一版本
        :return:
        """

        deployment = client.ExtensionsV1beta1DeploymentRollback(
            name=deployment_name,
            rollback_to= client.ExtensionsV1beta1RollbackConfig(
                revision=0
            )
        )

        return deployment

    def rollback_deployment(self, api_instance, namespace="default", deployment_name=""):

        api_response = api_instance.create_namespaced_deployment_rollback(
            name=deployment_name,
            namespace=namespace,
            body=self.rollback_deployment_object(deployment_name=deployment_name)
        )
        print(api_response.status)

    def all_deployment(cls, api_instance, namespace):
        "获取deployment状态"
        try:
            api_response = api_instance.list_namespaced_deployment(
                namespace=namespace,
            )
            return True, api_response
        except rest.ApiException as e:
            return False, "status code:{}, Reason:{}".format(e.status, e.reason)

    # service 相关

    def get_service_status(self, name, namespace="default"):
        "获取deployment状态"
        try:
            api_response = self.v1.read_namespaced_service_status(
                name=name,
                namespace=namespace
            )
            return True, api_response
        except rest.ApiException as e:
            return False, "status code:{}, Reason:{}".format(e.status, e.reason)

    def create_service_object(self,name, type, ports, selector):
        """
        实例化service body对象
        :return:
        """
        if not ports:
            return False, "没有设定端口"

        _tmp_port = []
        for port in ports:
            _tmp_port.append(client.V1ServicePort(**port))

        # service 载体
        spec = client.V1ServiceSpec(
            type=type,
            ports=_tmp_port,
            selector=selector
        )

        # 实例化 service 对象
        service = client.V1Service(
            api_version="v1",
            kind="Service",
            metadata=client.V1ObjectMeta(name=name, labels=selector),
            spec=spec
        )

        return service

    # pod 相关
    def get_pod_status(self, name, namespace="default"):
        "获取pod状态"
        try:
            api_response = self.v1.read_namespaced_pod(
                name=name,
                namespace=namespace
            )
            return True, api_response
        except rest.ApiException as e:
            return False, "status code:{}, Reason:{}".format(e.status, e.reason)

    def main(self):
        extensions_v1beta1 = client.ExtensionsV1beta1Api()

        selector = {"match_labels": {"project": "www", "app": "java-demo"}}

        volumes = {"name": "test-hostpath", "host_path": {"path": "/tmp"}}

        probe = {"initial_delay_seconds": 60, "timeout_seconds": 20, "http_get": {"port": 8014, "path": "/"}}

        resources = {"requests": {"cpu": "0.5", "memory": "1Gi"}, "limits": {"cpu": "1", "memory": "2Gi"}}

        containers = [{
            "name": "tomcat",
            "image": "harbor.reapal.com/library/reapal-cloud-web:v1.0.3",
            "image_pull_policy": "Always",
            "volume_mounts": [{"name": "test-hostpath", "mount_path": "/tmp"}],
            "ports": [{"name": "web", "container_port": 80}]
        }]

        # 创建deployment
        # deployment = self.create_deployment_object(
        #     name="reapal-cloud-web",
        #     labels={"project": "www", "app": "java-demo"},
        #     selector=selector,
        #     resources=resources,
        #     replicas=1,
        #     volumes=volumes,
        #     containers=containers,
        #     probe=probe
        # )
        # self.create_deployment(extensions_v1beta1,deployment_body=deployment)

        # 升级deployment
        # self.update_deployment(
        #     "reapal-cloud-web",
        #     extensions_v1beta1,
        #     deployment,
        #     image="harbor.reapal.com/library/reapal-cloud-web:v1.0.4")

        # 删除deployment
        # self.delete_deployment("reapal-cloud-web", extensions_v1beta1)

        # service 创建 标签 app=nginx

        service_body = self.create_service_object(
            name="reapal-cloud-web",
            type="NodePort",
            ports=[{"name":"web", "port":8014, "target_port":8014}],
            selector={"project":"www", "app":"java-demo"}
        )
        api_respones = self.v1.create_namespaced_service(namespace="default", body=service_body, pretty="true")
        print(str(api_respones.status))

        # deployment 回滚上一个版本
        # self.rollback_deployment(extensions_v1beta1)

        # from_to_yaml
        # aa = self.create_from_yaml("java_getway.yaml")
        # print(aa)
        # deployment_status, deployment = self.get_deployment_status(extensions_v1beta1, name="reapal-cloud-web", namespace="default")
        # print(deployment)
        # print(deployment.spec.template.spec.containers[0].image)
        # self.update_deployment(
        #     "reapal-cloud-web",
        #     extensions_v1beta1,
        #     deployment,
        #     image="harbor.reapal.com/library/reapal-cloud-web:v1.0.4")
        # print(self.get_service_status(name="reapal-cloud-web", namespace="default"))
        # aa = self.get_deployment_list(api_instance=extensions_v1beta1, namespace="default")
        # print(aa)
        # pods = self.get_pod_status(name="reapal-cloud-web-755499c758-h4wvm")
        # print(pods)
        # service_status = self.get_service_status(name="reapal-cloud-web")
        # print(service_status)
        # 创建命名空间
        # aa = self.create_from_yaml("namespace.yaml")
        # print(aa)
        # body = client.V1Namespace()
        # self.v1.create_namespace(body=body, name="TestEnvironment")
        # aa = client.V1ContainerImage(names=["harbor.reapal.com/library/reapal-cloud-web:v2.0.4"])
        # print(aa)


if __name__ == '__main__':
    api = MyKubernetesApi()
    api.main()
