#! /usr/bin/[ython
# -*- coding=utf-8 -*-
"""
编写一个多线程抓取网页的程序，并阐明多线程抓取程序是否可比单线程性能有提升
"""
from threading import Thread
from urllib.request import Request
from queue import Queue
from lxml import etree
import requests
from threading import Lock
import time

#获取诗歌对应得网址和诗歌对应得网址
class Process(Thread):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400"}
    def run(self):
        global url_quene,class_poem_queue,p_lock,t_lock
        while True:
            #诗歌分类得url取完，结束任务
            if class_poem_queue.empty():
                break
            else:
                url_main = class_poem_queue.get()
            req = requests.get(url=url_main,headers=self.headers)
            html_parser = etree.HTMLParser(encoding="utf-8")
            html_elements = etree.HTML(req.text,parser=html_parser)
            urls = html_elements.xpath("//div[@class='sons']//div[@class='cont']//a/@href")
            for url in urls:
                if class_poem_queue.full():
                    pass
                else:
                    #由于分类得url没有协议与域名，只有后缀，所欲通过协议是否在url中判断是否为分类得url
                    if "http" not in url:
                        url = "https://www.gushiwen.org/" + url
                        class_poem_queue.put(url)
                    else:
                        p_lock.acquire()
                        if url_quene.full():
                            url_quene.join()
                        else:
                            url_quene.put(url)
                        p_lock.release()
#爬取诗歌并打印
class Consumer(Thread):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400"}
    def run(self):
        global url_quene
        while True:
            if url_quene.empty():
                print(self.name)
                break
            #创建锁，对url_queue不能同时访问
            p_lock.acquire()
            url = url_quene.get()
            p_lock.release()
            req = requests.get(url=url, headers=self.headers)
            html_parser = etree.HTMLParser(encoding="utf-8")
            html_elements = etree.HTML(req.text, parser=html_parser)
            texts = html_elements.xpath("//div[@class='contson']//span/text()")
            for text in texts:
                print(text)


if __name__ == '__main__':
    url = "https://www.gushiwen.org/shiju/shuqing.aspx"
    url_quene = Queue(1000)
    class_poem_queue = Queue(100)
    class_poem_queue.put(url)
    p_lock = Lock()
    p1 = Process(name="11")
    p1.start()
    for i in range(40):
        c = Consumer(name="threadingConsumer%d"%i)
        time.sleep(1)
        c.start()