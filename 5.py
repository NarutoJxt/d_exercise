#! /usr/bin/[ython
# -*- coding=utf-8 -*-

"""
用python实现统计一篇英文文章内每个单词的出现频率，
并返回出现频率最高的前10个单词及其出现次数，并解答以下问题？（标点符号可忽略）
"""
import re
from collections import Counter
# text = ""
#打开文件，读取每一行放入text中
def open_wi_space():
    text = ""
    with open("2.txt","r") as fp:
        for vals in fp.readlines():
            vals = vals.strip()#去除每一行的换行
            text+=vals
    # 把以空格分开作为一个单词
    val_list = text.split(" ")
    return val_list

"""
（2）追加需求：引号内元素需要算作一个单词，如何实现？
"""
def open_with_word():
    import re
    from collections import Counter

    with open('2.txt', 'r', ) as f:
        words = f.read()  # 将文件的内容全部读取成一个字符串

        count = Counter(re.split(r"\W+", words))  # 以单词为分隔

    result = count.most_common(10)  # 统计最常使用的前10个
    print(result)
def read_text_without_quote():
    with open("2.txt") as file_1:
        tmp_list1 = []
        for line in file_1.readlines():
            tmp_list = line.split('"')
            for index in range(len(tmp_list)):
                if (index + 1) % 2 != 0:
                    tmp_list_handle = tmp_list[index].strip()
                    tmp_list2 = tmp_list_handle.split()
                    tmp_list1.extend(tmp_list2)
                else:
                    tmp_list1.extend([tmp_list[index]])
        print(tmp_list1)
        count1 = Counter(tmp_list1)
        print(count1.most_common(10))
if __name__ == '__main__':
    read_text_without_quote()



