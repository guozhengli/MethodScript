#!/usr/env python
# -*- coding:utf8 -*-
__author__ = '李国征'
__email__ = "745292907@qq.com"

from kubernetes import client


def change(dct, obj):
    # 内容转换 如果不存在输出obj 否则把dct当作参数传递给obj
    try:
        if not dct:
            return False, obj()
        return True, obj(**dct)
    except:
        return False, obj()


def deployment(dct):
    """
    传入 dict格式数据 输出body数据
    :param dct:
    :return: body -> dict
    dct = {
        "api_version":"apps/v1",
        "kind":"Deployment",
        "metadata":{"name": "nginx-deployment", "labels":{"app": "nginx"}},
        "spec":{
            "replicas":3,
            "selector": {"match_labels":{"app": "nginx"}},
            "template": {
                "metadata":{"labels":{"app": "nginx"}},
                "spec": {
                    "containers":[{"name":"nginx","image":"nginx", "ports": [{"container_port":80}] }]
                }
            }
        }
    }
    """
    v1_container_port = client.V1ContainerPort()
    v1_container = client.V1Container()
    v1_object_meta = client.V1ObjectMeta()
    v1_pod_templates_pec = client.V1PodTemplateSpec()
    v1_label_selector = client.V1LabelSelector()
    v1_deployment_spec = client.V1DeploymentSpec(template=v1_pod_templates_pec, selector=v1_label_selector)

    body_metadata = dct.pop("metadata", v1_object_meta)
    dct["metadata"] = body_metadata

    body_spec = dct.pop("spec", v1_deployment_spec)
    if not isinstance(body_spec,dict):
        dct['spec'] = body_spec
        return client.V1Deployment(**dct)

    spec_selector = body_spec.pop("selector", v1_label_selector)
    if not isinstance(spec_selector, dict):
        body_spec['selector'] = spec_selector
        dct['spec'] = body_spec
        return client.V1Deployment(**dct)

    spec_template = body_spec.pop("template", v1_pod_templates_pec)
    if not isinstance(spec_template, dict):
        body_spec["template"] = spec_template
        body_spec['selector'] = spec_selector
        dct['spec'] = body_spec
        return client.V1Deployment(**dct)

    template_metadata = spec_template.pop("metadata", v1_object_meta)
    if not isinstance(template_metadata, dict):
        spec_template['metadata'] = template_metadata
        body_spec["template"] = spec_template
        body_spec['selector'] = spec_selector
        dct['spec'] = body_spec
        return client.V1Deployment(**dct)

    template_spec = spec_template.pop("spec", v1_object_meta)
    if not isinstance(template_spec, dict):
        spec_template['spec'] = template_spec
        spec_template['metadata'] = template_metadata
        body_spec["template"] = spec_template
        body_spec['selector'] = spec_selector
        dct['spec'] = body_spec
        return client.V1Deployment(**dct)

    template_spec_containers = template_spec.pop("containers", v1_container)
    if not isinstance(template_spec_containers, dict):
        template_spec['containers'] = template_spec_containers
        spec_template['metadata'] = template_spec
        body_spec["template"] = spec_template
        body_spec['selector'] = spec_selector
        dct['spec'] = body_spec
        return client.V1Deployment(**dct)

    template_spec_containers_ports = template_spec_containers.pop("ports", v1_container_port)
    if not isinstance(template_spec_containers_ports, dict):
        template_spec_containers['ports'] = template_spec_containers
        template_spec['containers'] = template_spec_containers
        spec_template['metadata'] = template_spec
        body_spec["template"] = spec_template
        body_spec['selector'] = spec_selector
        dct['spec'] = body_spec
        return client.V1Deployment(**dct)

    template_spec_containers['ports'] = client.V1ContainerPort(template_spec_containers)
    template_spec['containers'] = client.V1Container(template_spec_containers)
    spec_template['spec'] = client.V1ObjectMeta(**template_spec)
    spec_template['metadata'] = client.V1ObjectMeta(**template_metadata)
    body_spec['template'] = client.V1PodTemplateSpec(**spec_template)
    body_spec['selector'] = client.V1LabelSelector(**spec_selector)
    dct['spec'] = body_spec

    body = client.V1Deployment(**dct)
    return body


def service(dct):
    """
    传入 dict格式数据 输出body数据
    :param dct:
    :return:
    dct = {
        "api_version": "v1",
        "kind": "Service",
        "metadata": {
            "name": "nginx-service",
            "labels": {"app": "nginx"}
        },
        "spec": {
            "type": "NodePort",
            "ports": [{
                "port": 80,
                "target_port": 80
            }],
            "selector": {"app": "nginx"}
        }
    }
    """

    try:
        v1_object_meta = dct.get("metadata", client.V1ObjectMeta())
        dct['metadata'] = client.V1ObjectMeta(**v1_object_meta)
    except:
        dct['metadata'] = client.V1ObjectMeta()

    try:
        v1_object_spec = dct.get("spec", client.V1ServiceSpec())
        dct['spec'] = client.V1ServiceSpec(**v1_object_spec)
    except:
        dct['spec'] = client.V1ServiceSpec()

    try:
        _tmp_list = []
        v1_service_port = dct["spec"]["ports"]
        if v1_service_port > 1:
            for i in v1_service_port:
                _tmp_list.append(client.V1ServicePort(**i))
        dct['spec']["ports"] = _tmp_list
    except:
        pass

    service_body = client.V1Service(**dct)
    return service_body
