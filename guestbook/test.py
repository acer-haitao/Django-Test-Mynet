#!/usr/bin/python
# -*- coding: UTF-8 -*-
#########################################################################
# File Name: addreplace.py
# Author: yuhaitao
# mail: acer_yuhaitao@163.com
# Created Time: Fri 31 Mar 2017 07:05:13 PM PDT
#########################################################################
import pymysql
import sqlite3

def DbSongName(song_id,cursor):
    sql_song_name = """SELECT * FROM  music163 WHERE song_id = %s """ %(song_id)
    try:
        cursor.execute(sql_song_name)
        results = cursor.fetchall()
        for row in results:
            name = row[2]
    except:
        print("======")
    return name



def DBinsert():
    db = pymysql.connect("bdm273925510.my3w.com","bdm273925510","haitao131","bdm273925510_db",charset='utf8' )
    cursor = db.cursor()
    sql ='''SELECT * FROM  comment163 WHERE liked  > %s order by liked DESC ; ''' %(1)
    cursor.execute(sql)
    results = cursor.fetchall()
    for i, row in enumerate(results):
        id = row[0]
        song_id = row[1]
        # print song_id
        song_name = DbSongName(song_id, cursor)
        # print song_name
        txt = row[2]
        author = row[3]
        liked = row[4]
        footer = '序号:%s--歌名:%s--评论数:%s--%s' % (i, song_name, liked, author)
        print(txt,footer)
        sqlitetest(txt,footer)
def sqlitetest(txt,footer):
    cx = sqlite3.connect("D:\Python-Test\StuProject\db.sqlite3")
    cu = cx.cursor()
    #sql = '''insert into 'comment_comment'(txt,'footer') values (\"%s\",\"%s\");'''%(pymysql.escape_string(txt),pymysql.escape_string(footer))#字符串插入字符串sql
    sql = '''insert into 'comment_comment'(txt,'footer') values (\"%s\",\"%s\");''' % (txt, footer)  # 字符串插入字符串sql
    try:
        cu.execute(sql)
        cx.commit()
    except Exception as e:
        with open("D:\Python-Test\StuProject\dblog.txt",'a+') as f:
            log = '''执行sql发生错误:%s \n 输出:%s'''%(e,sql)
            #f.write(log)
        pass
    print(cu)
DBinsert()