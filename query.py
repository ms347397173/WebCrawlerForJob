import MySQLdb

conn=MySQLdb.Connect(
		host='127.0.0.1',
		port=3306,
		user='root',
		passwd='m',
		charset='utf8'
		)

cursor=conn.cursor()
cursor.execute("set names utf8")
cursor.execute('use job')
cursor.execute('select * from job_xjtu_info')
rs=cursor.fetchmany(3)
print rs
