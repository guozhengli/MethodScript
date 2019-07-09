#!/usr/env python
# -*- coding:utf8 -*-
__author__ = '李国征'
__email__ = "745292907@qq.com"

from kubernetes import client, config
from pprint import pprint


def main():

    config.load_kube_config(config_file="admin-role.yaml")

    v1 = client.CoreV1Api()
    apps_v1 = client.AppsV1Api()

    # for ns in v1.list_namespace().items:
    #     print(ns.metadata.name)
    # print("Listing pods with their IPs:")
    # ret = v1.list_pod_for_all_namespaces(watch=False)
    # for i in ret.items:
    #     print("%s\t%s\t%s" %
    #           (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

    namespace = "default"

    # deployment 创建
    # template_metadata = client.V1ObjectMeta(name="nginx-deployment", labels={"app": "nginx"})
    #
    # template_spec_containers_ports = client.V1ContainerPort(container_port=80)
    #
    # template_spec_containers = client.V1Container(name="nginx", image="nginx:latest")
    # template_spec_containers.ports = [template_spec_containers_ports]
    #
    # template_spec = client.V1PodSpec(containers=[template_spec_containers])
    #
    # spec_template = client.V1PodTemplateSpec(metadata=template_metadata, spec=template_spec)
    #
    # spec_selector = client.V1LabelSelector(match_labels={"app": "nginx"})
    #
    # spec = client.V1DeploymentSpec(replicas=2, template=spec_template, selector=spec_selector)
    #
    # body = client.V1Deployment(kind="Deployment", spec=spec, metadata=template_metadata)
    #
    # print(body)
    # pretty = 'true'
    # api_response = apps_v1.create_namespaced_deployment(namespace, body, pretty=pretty)
    # pprint(api_response)

    print('#' * 100)

    # pod 创建
    # body = client.V1Pod(
    #     api_version="v1",
    #     kind="Pod",
    #     metadata=client.V1ObjectMeta(
    #         name = "mypod"
    #     ),
    #     spec=client.V1PodSpec(
    #         containers = [client.V1Container(
    #             name = "nginx",
    #             image = "nginx:1.14",
    #         )]
    #     ),
    # )
    #
    # pretty = 'true'
    # api_response = v1.create_namespaced_pod(namespace, body, pretty=pretty)
    # pprint(api_response)

    # 启动外网可访问的nginx 实例
    # Deployment
    # body = client.V1Deployment(
    #     api_version="apps/v1",
    #     kind="Deployment",
    #     metadata=client.V1ObjectMeta(
    #         name="nginx-deployment",
    #         labels={"app":"nginx"}
    #     ),
    #     spec=client.V1DeploymentSpec(
    #         replicas=3,
    #         selector=client.V1LabelSelector(
    #             match_labels={"app": "nginx"}
    #         ),
    #         template=client.V1PodTemplateSpec(
    #             metadata=client.V1ObjectMeta(
    #                 labels={"app": "nginx"}
    #             ),
    #             spec=client.V1PodSpec(
    #                 containers=[client.V1Container(
    #                     name="nginx",
    #                     image="nginx:1.15.4",
    #                     ports=[client.V1ContainerPort(
    #                         container_port=80
    #                     )]
    #                 ),
    #                 ]
    #             )
    #         )
    #     )
    #
    # )
    #
    # pretty = "true"
    # api_response = apps_v1.create_namespaced_deployment(namespace, body, pretty=pretty)
    # pprint(api_response)
    # print("^  to  Deployment")
    #
    # # Service
    # service_body = client.V1Service(
    #     api_version="v1",
    #     kind="Service",
    #     metadata=client.V1ObjectMeta(
    #         name="nginx-service",
    #         labels={"app": "nginx"}
    #     ),
    #     spec=client.V1ServiceSpec(
    #         type="NodePort",
    #         ports=[client.V1ServicePort(
    #             port=80,
    #             target_port=80,
    #             node_port=38100
    #         )],
    #         selector={"app": "nginx"}
    #     )
    # )
    # pretty = "true"
    # vi_respones = v1.create_namespaced_service(namespace, service_body, pretty=pretty)
    # print('#'*100)
    # print("v  to Service")
    # pprint(vi_respones)



if __name__ == '__main__':
    main()
