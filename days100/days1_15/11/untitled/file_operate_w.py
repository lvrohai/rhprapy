from math import sqrt

def is_prime(n):
    """ 判断素数 """
    assert n > 0
    for f in range(2, int(sqrt(n))+1):
        if n % f == 0:
            return False
    return True if n != 1 else False

def main():
    filenames = ('a.txt','b.txt','c.txt')
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename,'w',encoding='utf-8'))
        for number in range(2, 10000):
            if is_prime(number):
                if number<100:
                    fs_list[0].write(str(number) + '\n')
                elif number < 1000:
                    fs_list[1].write(str(number) + '\n')
                else:
                    fs_list[2].write(str(number) + '\n')
    except IOError as ex:
        print(ex)
        print("io错误")
    for fs in fs_list:
        fs.close()
    print("结束")

if __name__ == '__main__':
    print(is_prime(4))
    main()