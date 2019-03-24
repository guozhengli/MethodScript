#!/usr/env python
# -*- coding:utf8 -*-
__author__ = '李国征'
__email__ = "745292907@qq.com"
import sys
import subprocess
import pexpect


def __connect_cisco_vpn__(username, pwd, domain):

    # 命令串cmd
    credentials = "printf '" +"y\\n"  + username + "\\ny" + pwd + "\\ny'"
    # credentials = "printf '" + "y\\n"  + username + "\\ny" + pwd + "\\ny'"
    vpn_cmd = "/opt/cisco/anyconnect/bin/vpn -s connect '" + domain + "'"
    cmd = credentials + " | " + vpn_cmd

    # 打印命令串
    print("命令行: \n" + cmd)
    # subprocess.Popen(cmd,
    #                  shell=True,
    #                  stdout=subprocess.PIPE,
    #                  stderr=subprocess.PIPE).communicate()


def connection(domain, username, password):
  child = pexpect.spawn('/opt/cisco/anyconnect/bin/vpn connect ' + domain, maxread=2000)
  # child.logfile = sys.stdout
  cc = child.expect(['Connect Anyway? [y/n]:.*', pexpect.TIMEOUT, pexpect.EOF])
  child.sendline('y')
  child.expect('Username: \[.*\]')
  child.sendline(username)
  child.expect('Password:')
  child.logfile = None
  child.sendline(password)
  # child.expect('accept? [y/n]: \[.*\]')
  # child.sendline("y")
  child.logfile = sys.stdout
  child.expect('  >> notice: Please respond to banner.')
  child.delaybeforesend = 1
  child.sendline('y')
  child.expect('  >> state: Connected')

if __name__ == '__main__':
    # __connect_cisco_vpn__('ligz', 'ligz@0123', '119.254.149.68')
    connection('119.254.149.68', "ligz", "ligz@0123")

