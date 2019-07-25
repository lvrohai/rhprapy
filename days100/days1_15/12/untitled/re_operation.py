import re

def main():
    username=input("请输入用户名")
    qq = input("请输入QQ")
    # match方法的第一个参数是正则表达式字符串或正则表达式对象
    # 第二个参数是要跟正则表达式做匹配的字符串对象
    # 用正则表达式匹配字符串 成功返回匹配对象 否则返回None
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$',username)
    if not m1:
        print('请输入有效的用户名')
    m2 = re.match(r'^[1-9]\d{4,11}$',qq)
    if not m2:
        print('请输入有效的QQ号')
    if m1 and m2:
        print('输入都有效')

def main1():
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    sentence = '''
        重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
        不是15600998765，也是110或119，王大锤的手机号才是15600998765。
        '''
    # 查找所有匹配并保存到一个列表中
    mylist = re.findall(pattern,sentence)
    print(mylist)
    print('-----------------------------')
    # 通过迭代器取出匹配对象并获得匹配的内容
    # 查找字符串所有与正则表达式匹配的模式 返回一个迭代器
    # print(pattern.finditer(sentence))
    for temp in pattern.finditer(sentence):
        print(temp.group())
    print('-----------------------------')
    # 通过search函数指定搜索位置找出所有匹配
    m = pattern.search(sentence)
    while m:
        print('m->'+ str(m))
        print(m.group())
        print(m.groups())
        print(m.end())
        m = pattern.search(sentence,m.end())

def main2():
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    #  sub(pattern, repl, string, count=0, flags=0)用指定的字符串替换原字符串中与正则表达式匹配的模式 可以用count指定替换的次数
    purified = re.sub(r'[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔','*',sentence,flags=re.IGNORECASE)
    print(purified)

def main3():
    poem = ',窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
    # split(pattern, string, maxsplit=0, flags=0)用正则表达式指定的模式分隔符拆分字符串 返回列表
    sentence_list = re.split(r'[,.，。]',poem)
    print(sentence_list)
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)


if __name__ == '__main__':
    main3()
