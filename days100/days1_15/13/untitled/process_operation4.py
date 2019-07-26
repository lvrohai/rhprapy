from multiprocessing import Process, Queue
from time import sleep

def sub_task(q, str, n):
    i = 0
    while i < n:
        q.put(str)
        i += 1
        sleep(1)

def main():
    q = Queue()
    p1 = Process(target=sub_task,args=(q,'Ping',5))
    p2 = Process(target=sub_task,args=(q,'Pang',5))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    while not q.empty():
        print(q.get())

if __name__ == '__main__':
    main()