# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# asyncio1.py

import time

def hello():
    time.sleep(1)

def run():
    for i in range(5):
        hello()
        print('Hello World:%s' % time.time())

if __name__ == '__main__':
    run()
