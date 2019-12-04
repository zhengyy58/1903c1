import sqlite3

conn = sqlite3.connect("1903c.db")

cur = conn.cursor()

# cur.execute("CREATE TABLE student(id INTEGER PRIMARY KEY AUTOINCREMENT,"
#                                     "name CHAR(5) not null,"
#                                     "age INTEGER)")

# cur.execute("DROP TABLE student")
# cur.execute("INSERT INTO student VALUES (1,'张三',40)")
# a = "李四"
# cur.execute("INSERT INTO student (age) VALUES (?)",(18,))
# cur.execute("UPDATE student SET name='小明',age=20")
# cur.execute("UPDATE student SET name='小刚',age=30 WHERE id=1")
# name = cur.execute("SELECT id FROM student WHERE name like '_%'")
# print(name.fetchall())
# print(name.fetchone())


cur.execute("PRAGMA foreign_keys=on")
# cur.execute("CREATE TABLE a (id INTEGER PRIMARY KEY  AUTOINCREMENT,"
#                             "name CHAR(5))")
# cur.execute("CREATE TABLE b (id INTEGER PRIMARY KEY  AUTOINCREMENT,"
#                             "age INTEGER,"
#                             "num INTEGER,"
#                             "foreign key (num) references a(id))")

a = cur.execute("SELECT num FROM b WHERE num=1")
print(a.fetchall())


conn.commit()
conn.close()

