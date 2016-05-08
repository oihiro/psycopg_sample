import psycopg2

conn = psycopg2.connect("dbname=tmp1 user=hiro")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS test;")
cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
cur.execute("INSERT INTO test (num, data) VALUES(%s, %s);", (100, "abcdef"))
cur.execute("SELECT * FROM test;")
s = cur.fetchone()
print s
conn.commit()
cur.close()
conn.close()
