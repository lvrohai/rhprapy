from random import randint
from threading import Thread
from time import sleep, time

def download(filename):
    print('开始下载%s' % filename)
    time_to_download = randint(5,10)
    sleep(time_to_download)
    print('%s下载完成，花费了%d秒' % (filename,time_to_download))

def main():
    start = time()
    t1 = Thread(target=download,args=('Python入门到住院',))
    t1.start()
    t2 = Thread(target=download,args=('Tokyo hot.avi',))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.3f秒' % (end-start))

if __name__ == '__main__':
    main()