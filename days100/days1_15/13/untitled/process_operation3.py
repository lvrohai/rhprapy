from multiprocessing import Process, Queue

def f1(queue):
    for i in range(10):
        queue.put(i)

def f2(queue):
    for i in range(10):
        print(queue.get())

def main():
    q = Queue()
    Process(target=f1,args=(q,)).start()
    Process(target=f2,args=(q,)).start()

if __name__ == '__main__':
    main()