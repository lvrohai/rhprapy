# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# asyncio2.py

import time
import asyncio

async def hello(i):
    await asyncio.sleep(20)
    print('%d:Hello World:%s' % (i,time.time()))

def run():
    for i in range(5):
        loop.run_until_complete(hello(i))

loop = asyncio.get_event_loop()

if __name__ == '__main__':
    run()