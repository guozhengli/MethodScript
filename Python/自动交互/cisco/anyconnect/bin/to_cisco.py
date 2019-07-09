#!/usr/env python
# -*- coding:utf8 -*-
__author__ = '李国征'
__email__ = "745292907@qq.com"


import pexpect
import sys
import argparse

CISCO_USER = 'ligz'
CISCO_PWD = 'ligz925'
CISCO_HOST = '124.251.16.196'
CISCO_PATH = '/opt/cisco/anyconnect/bin/vpn'


class CiscoAnyconnect(object):
    """
    def __init__(self, command, args=[], timeout=30, maxread=2000,
                 searchwindowsize=None, logfile=None, cwd=None, env=None,
                 ignore_sighup=False, echo=True, preexec_fn=None,
                 encoding=None, codec_errors='strict', dimensions=None,
                 use_poll=False):
    """

    def __init__(self,  command, timeout=30, host=CISCO_HOST, cisco_user='', cisco_pwd="", status="start"):
        self.command = command
        self.cisco_user = cisco_user
        self.cisco_pwd = cisco_pwd
        self.timeout = timeout
        self.status = status
        self.host = host
        self.child = pexpect.spawn(self.command, timeout=timeout)

    def save_log(self, file_path):
        # 保存日志信息
        # file_path : 文件绝对路径

        self.child.logfile = open(file_path, 'wb+')

    def get_status(self):
        # 获取当前连接状态
        # return True or False
        self.child.expect("VPN>.*")
        self.child.sendline("state")
        status = bytes.decode(self.child.before)
        if "state: Disconnected" in status:
            return False
        if "state: Connected" in status:
            return True

    def is_running(self):
        # 是否已经运行中
        pass

    def close_connect(self):
        # 关闭运行中连接
        self.child.expect("VPN>.*")
        self.child.sendline("exit")

    def is_localConnect(self):
        # 判断当前连接ip 是否为本次连接ip
        # 如果是则返回true 否则返回 false
        pass

    def stop_connect(self):
        # 判断当前是否有连接 如果有则停止连接

        status = self.get_status()
        if status:
            self.child.expect(".*VPN>.*")
            self.child.sendline("disconnect")
            print("连接已断开！")
            print(self.child.before)
            return
        print("没有可停用的连接！")
        return

    def connect(self):
        # 连接vpn
        try:
            self.child.expect(".*VPN>.*")
            self.child.sendline("connect {}".format(self.host))
            i = self.child.expect('Connect Anyway?.*')
            if i == 0:
                print("进行VPN连接...")
                # self.child.logfile = open(file_path, 'wb+')
                self.child.sendline("yes")
                self.child.expect('.*Username:.*')
                self.child.sendline(self.cisco_user)
                self.child.expect('.*Password:.*')
                self.child.sendline(self.cisco_pwd)
                s = self.child.expect([".*accept?.*", ".*VPN>.*"])
                if s == 0:
                    self.child.sendline("y")
                elif s == 1:
                    self.child.sendline("exit")
                # self.child.close()
        except:
            status = client.get_status()
            if status:
                print("VPN连接成功！")
            else:
                print("VPN连接失败！")

    def crontab_status(self):
        # 放入执行

        # 判断当前是否有连接
        status = self.get_status()
        if not status:
            # 进行连接
            print("没有连接VPN，等待连接！")
            self.connect()
        else:
            print("已经连接，无需再次连接！")

    def force_connect(self):
        #强制连接
        c_status = self.get_status()
        print(c_status)
        if not c_status:
            self.connect()
            return
        self.stop_connect()
        # self.connect()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Cisco Anyconnect Python版本')
    parser.add_argument("-H", "--host", required=True, default=CISCO_HOST, help=u"填入VPN服务器IP地址")
    parser.add_argument("-u", "--user", default=CISCO_USER, help=u"填入用户名,默认为CISCO_USER所设置的值")
    parser.add_argument("-p", "--password", default=CISCO_PWD, help=u"填入密码,默认为CISCO_PWD所设置的值")
    parser.add_argument("-t", "--timeout", default=30, type=int, help=u"填入超时时间，默认为30秒")
    parser.add_argument("-r", "--releases", default=0, type=int, help=u"填入重试次数，默认不重试")
    parser.add_argument("-f", "--force", action="store_true", help=u"强制拨入")
    parser.add_argument("-s", "--status",required=True, default='start', help=u"status、start、stop、crontab、force")

    args = parser.parse_args()
    c_host = args.host;c_user = args.user;c_pwd = args.password;timeout = args.timeout;releases = args.releases
    c_timeout = args.timeout

    if not c_host or not c_user or not c_pwd:
        print("请设置默认值属性！host:{}, user:{}, password:{}".format(c_host, c_user, c_pwd))
        sys.exit(1)

    cmd = '{} -s '.format(CISCO_PATH)
    print('VPN程序路径-->', cmd)
    print("user password -->", c_user, c_pwd)
    client = CiscoAnyconnect(cmd,
                             host = c_host,
                             timeout=c_timeout,
                             cisco_user=c_user,
                             cisco_pwd=c_pwd,
                             status=args.status
                             )
    client.save_log("/tmp/logfile.txt")

    if args.force:
        # 检测当前状态 如果是连接状态
        # 会强制停掉然后进行再次拨入

        client.force_connect()
        client.close_connect()
        sys.exit(1)

    if args.status == "start":
        # 进行连接vpn
        client.connect()
        client.close_connect()
    elif args.status == "status":
        # 检查当前状态
        status = client.get_status()
        if not status:
            print("没有连接的vpn")
            sys.exit(1)
        print("已经连接vpn")
        client.close_connect()
        sys.exit(1)
    elif args.status == "stop":
        # 关闭现有连接
        client.stop_connect()
        client.close_connect()
    elif args.status == "crontab":
        # 放入crontab中执行使用

        client.crontab_status()
        client.close_connect()
    else:
        print("status 输入未知参数！")
        sys.exit(1)
