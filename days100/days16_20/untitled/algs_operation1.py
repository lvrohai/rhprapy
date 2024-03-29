# 顺序查找和二分查找
from math import log2, factorial

def seq_search(items: list, elem) -> int:
    """顺序查找"""
    # 对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），enumerate将其组成一个索引序列，利用它可以同时获得索引和值
    for index, item in enumerate(items):
        if elem == item:
            return index
    return -1

def bin_search(items, elem):
    """二分查找"""
    start,end = 0,len(items) - 1
    while start<=end:
        mid = int(start + (end-start)//2)
        if elem > items[mid]:
            start = mid + 1
        elif elem < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1

