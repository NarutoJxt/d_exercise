#! /usr/bin/[ython
# -*- coding=utf-8 -*-
# ! /usr/bin/[ython
# -*- coding=utf-8 -*-
import pymysql
import xlrd


def con_mysql(list_cell):
    try:
        conn = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            database="test",
            charset="utf8"
        )
        cusor = conn.cursor()
        sql = """
            insert into testexcell (position,salary,company,address,experience,
            education,com_type,fin_situation,total_people)
            values (%s,%s,%s,%s,%s,%s,%s,%s,%s)
       """
        for cell in list_cell:
            cusor.execute(sql,cell)

    except Exception as e:
        print(e)
    else:
        return cusor,conn
def save_file(cusor):
    sql = """
        select * from testexcell
    """
    content = cusor.execute(sql)
    content = cusor.fetchall()
    with open("1.txt","w",encoding="utf8") as fp:
        for cells in content:
            for cell in cells:
                fp.write(cell)
    cusor.close()
def read_xlas(fina_name):
    bk = xlrd.open_workbook(filename=fina_name, encoding_override="gb2312")
    bk = bk.sheets()[0]
    bk_rows = bk.nrows
    bk_cols = bk.ncols
    list_cell = []
    for i in range(bk_rows):
        cell = []
        for j in range(bk_cols):
            cell.append(bk.cell_value(i,j))
        list_cell.append(cell)
    cusor,conn = con_mysql(list_cell)
    save_file(cusor)
    conn.close()
if __name__ == '__main__':
    read_xlas("./boss直聘python职位_2019-07-02.xls")