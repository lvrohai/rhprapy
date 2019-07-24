from math import sqrt
import json

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

def main1():
    try:
        with open("i_f04.png",'rb') as fs1:
            data = fs1.read()
            print(type(data))
        with open("i_f04_2.png",'wb')as fs2:
            fs2.write(data)
    except FileNotFoundError:
        print("无法打开文件")
    except IOError:
        print("io错误")
    print("结束")

def main2():
    mydict = {
        'name': 'Diogenes',
        'age' : 18,
        'email': 'd@163.com',
        'friends':['白熊','panda'],
        'cars':[
            {'brand':'BYD','max_speed':180},
            {'brand':'Audi','max_speed':280},
            {'brand':'Benz','max_speed':380}
        ]
    }
    try:
        with open('data.json','w',encoding='utf-8') as fs:
            json.dump(mydict,fs)
    except IOError as e:
        print(e)
    print('结束')

if __name__ == '__main__':
    print(is_prime(4))
    main2()