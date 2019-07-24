import time

def main_r():
    f = open('杜鹃鸟.txt','r',encoding='utf-8')
    print(f.read())
    f.close()

def main_r1():
    f = None
    try:
        f = open('杜鹃鸟.txt','r',encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('未找到文件')
    except LookupError:
        print('未知编码')
    except UnicodeDecodeError:
        print('解码错误')
    finally:
        if f:
            f.close()

def main_r2():
    try:
        with open('杜鹃鸟.txt','r',encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('未找到文件')
    except LookupError:
        print('未知编码')
    except UnicodeDecodeError:
        print('解码错误')

def main_r3():
    # 一次性读取整个文件的内容
    with open('杜鹃鸟.txt','r',encoding='utf-8') as f:
        print(f.read())
    print('________________________')

    # 通过for in 循环逐行读取
    with open('杜鹃鸟.txt','r',encoding='utf-8') as f:
        for line in f:
            print(line, end='')
            time.sleep(1)
    print()
    print('________________________')

    # 读取文件按行读取到列表中
    with open('杜鹃鸟.txt','r',encoding='utf-8') as f:
        lines = f.readline();
        print('这一次是：' + lines)
    print(lines)




if __name__ == '__main__':
    main_r3()