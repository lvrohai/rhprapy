from multiprocessing import Process, Pipe

def f1(conn):
    for i in range(10):
        conn.send(i)

def f2(conn):
    for i in range(10):
        print(conn.recv())

def main():
    conn1, conn2 = Pipe()
    Process(target=f1,args=(conn1,)).start()
    Process(target=f2,args=(conn2,)).start()

if __name__ == '__main__':
    main()