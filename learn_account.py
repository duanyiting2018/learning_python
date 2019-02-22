# -*- coding: utf-8 -*-
import sqlite3
conn=sqlite3.connect('account.db')
#create_sql='create table account( id INTEGER PRIMARY KEY AUTOINCREMENT,name text,date text,score int,remart text);'
#conn.execute(create_sql)
insert_sql='insert into account (name  ,date  ,score ,remart ) values(?,?,?,?) '
conn.execute(insert_sql,('Martin','20181026',4,'提问怎么调用两个类'))
corsors=conn.execute("select * from account")

print("Matin  学习记录 :")
for row in corsors:
    print(row)
 

corsors_sum=conn.execute("select sum(score) from account")
for row in corsors_sum:
    print("Total Scores: ",row[0])
conn.close()