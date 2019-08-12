# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# asyncio1.py

import asyncio
import time

def hello():
    time.sleep(1)

def run():
    for i in range(5):
        hello()
        print('Hello World:%s' % time.time())


async def add(x=1, y=2):
    print("Add {} + {} ...".format(x,y))
    await asyncio.sleep(2)
    return x + y

s = time.time()
loop = asyncio.get_event_loop()
tasks = [add(x,y) for x,y in zip(range(1,10),range(11,20))]
# loop.run_until_complete(add())
loop.run_until_complete(asyncio.wait(tasks))
print('cost:', time.time()-s)

if __name__ == '__main__':
   pass
