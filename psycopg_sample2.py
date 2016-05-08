#!/usr/bin/python
# -*- coding:utf-8 -*-
#
import psycopg2

conn = psycopg2.connect("dbname=tmp1 user=hiro")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS test;")
cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
data = ((100, 'あいうえお'), (200, 'かきくけこ'), (300, '昭和'))
cur.executemany("INSERT INTO test (num, data) VALUES(%s, %s);", data)
cur.execute("SELECT * FROM test;")
rows = cur.fetchall()
for row in rows:
    print row
    print type(row[2]),repr(row[2])
    print unicode(row[2], 'utf-8')
conn.commit()
cur.close()
conn.close()
