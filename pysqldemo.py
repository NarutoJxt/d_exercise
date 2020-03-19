#!/usr/bin/python3
# -*- coding=utf-8 -*-

import pymysql
conn = 0
def con():
    conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        database="test",
        charset="utf8"
    )
    return conn
def add():
    #创建连接对象
    conn=con()
    #生成一个用来执行sql语句的游标对象
    cursor=conn.cursor()
    #用repr（）函数将字符串进行处理之后才能给sql中的值传递
    sql="insert into student1 values(%d,%s,%d)"%(1003,repr('刘备2'),45)
    #通过游标进行提交
    cursor.execute(sql)
    #通过conn提交事务
    conn.commit()
    cursor.close()
    conn.close()

def searchAll():
    conn=con()
    cursor =conn.cursor()
    sql="select * from student1"
    cursor.execute(sql)
    #获得结果集
    result=cursor.fetchall()
    print(result)
    cursor.close()
    conn.close()
if __name__ == '__main__':
    searchAll()