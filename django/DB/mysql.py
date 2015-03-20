__author__ = 'zice'
#
# coding=utf-8
#
import MySQLdb

conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='test')
cur = conn.cursor()

cur.execute("select name from t1 limit 1,10")
name = [row[0] for row in cur.fetchall()]
print name
# create db
# cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")

# insert
# cur.execute("insert into student values('2','Tom','3 year 2 class','9')")


# query
# cur.execute("update student set class='3 year 1 class' where name = 'Tom'")

# delete
# cur.execute("delete from student where age='9'")

cur.close()
conn.commit()
conn.close()