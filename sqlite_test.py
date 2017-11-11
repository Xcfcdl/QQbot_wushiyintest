#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sqlite3
from collections import namedtuple
conn = sqlite3.connect('user_db.db')
print('open success')
c = conn.cursor()
"""c.execute('''CREATE TABLE COMPANY
          (ID INT PRIMARY KEY   NOT NULL,
          NAME            TEXT   NOT NULL,
          AGE             INT     NOT NULL,
          ADDRESS         CHAR(50),
          SALARY          REAL);''')"""
"""c.execute('''CREATE TABLE USERS 
          (
            QQ INT PRIMARY KEY, MODE VARCHAR(20), KANAGOALS FLOAT, TESTTIME INT
          )''')
"""
"""c.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) VALUES (1, 'pEER', 32, 'cASDLFJSDLF', 20000.00)")
c.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) VALUES (2, '2pEER', 12, 'cASDLFJ321SDLF', 10000.00)")"""
#c.execute("UPDATE COMPANY set ID = 321 where NAME='pEER'")
ins = 'insert into userS (qq, mode, kanagoals, testtime) VALUES(?, ?, ?, ?)'
c.execute(ins, ('746953609', 'kanatest', 0, 0))
cursor = c.execute("DELETE from users where qq='746953609'")
value = cursor.fetchall()
print(value)
print('created')
conn.commit()
conn.close()


def get_con(func):
    data_path = r"../user_db.db"
    def sql_exc():
        conn = sqlite3.connect(data_path)
        conn.text_factory = str
        cur = conn.cursor()
        func(cur)
        cur.close()
        conn.close()
    return sql_exc

@get_con
def get_users(cur):
    cur.execute("select * from users")
    rows = cur.fetchall()
    return rows

@get_con
def get_kana_model(cur):
    cur.execute("select * from kana_model")
    rows = cur.fetchall()
    return rows

@get_con
def get_kanagoals(cur):
    cur.execute("select * from kanagoals")
    rows = cur.fetchall()
    return rows
