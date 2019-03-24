#!/usr/env python
# -*- coding:utf8 -*-
__author__ = '李国征'
__email__ = "745292907@qq.com"

import docker

harbor_name = "admin"
harbor_pwd = "Harbor12345"
harbor_url = "10.168.16.103"


class DockerApi(object):
    """
    Docker 接口
    """

    def __init__(self, base_url):
        self.client = docker.DockerClient(base_url=base_url)

    def login(self):
        # 私有仓库登录
        l = self.client.login(username=harbor_name, password=harbor_pwd, registry=harbor_url)
        print(l)

    def get_node(self):
        # 获取所有节点
        # return obj list
        node_list = self.client.nodes.list()
        return node_list

    def get_service(self):
        # 获取所有服务
        service_list = self.client.services.list()
        return service_list

    def get_service_status(self, service_id):
        # 检查service是否存在
        # 获取到 反馈ID 获取不到返回False
        try:
            service = self.client.services.get(service_id=service_id)
            return service
        except Exception as e:
            print(e)
            return ""

    def scale(self, size, service_id):
        # 缩扩容 容器
        # return 状态，信息
        service_obj = self.get_service_status(service_id)
        if service_obj:
            try:
                service = getattr(service_obj, "scale")(size)
                return service
            except AttributeError as e:
                return False, e

    def upgrade(self, image, service_id):
        # 升级
        service_update_obj = self.get_service_status(service_id)
        if service_update_obj:
            try:
                service = getattr(service_update_obj, "update")(image=image)
                print(service)
                return service
            except AttributeError as e:
                print(e)
                return False, e

    def rollback(self, **kwargs):
        # 回滚
        pass

    def main(self):
        self.login()    # 进行仓库认证
        cc = self.get_service_status("4zbpbiialax7")
        print(dir(cc))
        # self.scale(2, "4zbpbiialax7")
        self.upgrade("10.168.16.103/library/nginx:1.13.3", "4zbpbiialax7")


if __name__ == '__main__':
    docker_api = DockerApi(base_url="tcp://10.168.16.103:7777")
    docker_api.main()



