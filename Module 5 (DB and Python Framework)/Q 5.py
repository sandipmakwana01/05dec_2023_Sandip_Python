# A QuerySet is a collection of data from a database. 
# A QuerySet is built up as a list of objects. 
# QuerySets makes it easier to get the data you actually need, by allowing you to filter and order the data at an early stage. 
# In this tutorial we will be querying data from the Member table.


import sqlite3

try:
    dbcon=sqlite3.connect("mydb.db")
    print("Databse connected")
except Exception as e:
    print(e)

# Table Create
tbl_create="create table studinfo(id integer primary key autoincrement,name text,sub text)"
try:
    dbcon.execute(tbl_create)
    print("Table created successfully!")
except Exception as e:
    print(e)

# Insert Records
"""insert_data="insert into studinfo(name,sub) values('sanket','python'),('mitesh','php'),('pratik','java'),('sunil','c++'),('nirav','android')"
try:
    dbcon.execute(insert_data)
    dbcon.commit()
    print("Record inserted successfully!")
except Exception as e:
    print(e)"""

# Update Records
update_data="update studinfo set sub='iOS' where sub='android'"
try:
    dbcon.execute(update_data)
    dbcon.commit()
    print("Record updated successfully!")
except Exception as e:
    print(e)

# Delete Records
# delete_data="delete from studinfo where id=2"
# try:
#     dbcon.execute(delete_data)
#     dbcon.commit()
#     print("Record deleted successfully!")
# except Exception as e:
#     print(e)


cur=dbcon.cursor()
# Show Records
show_data="select * from studinfo"
try:
    cur.execute(show_data)
    data=cur.fetchall()
    #data=cur.fetchmany(3)
    #data=cur.fetchone()
    #print(data)
    for i in data:
        print(i)
except Exception as e:
    print(e)