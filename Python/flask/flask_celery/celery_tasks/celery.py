#!/usr/bin/env python
# -*- coding:utf-8 -*-
from celery import Celery
from celery.schedules import crontab

cel = Celery('xxxxxx',
                broker='redis://192.168.11.91:6379',
                backend='redis://192.168.11.91:6379',
                include=['celery_tasks.tasks','celery_tasks.xxx'])

# # 时区
# celery.conf.timezone = 'Asia/Shanghai'
# # 是否使用UTC
# celery.conf.enable_utc = False