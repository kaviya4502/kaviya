import mysql.connector

con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_kavi"
)


def insert():
    name=input("enter your name:")
    email=input("enter your mail:")
    city=input("enter your city:")

    res=con.cursor()  
    sql="insert into user(name,email,city) values (%s,%s,%s)"
    res.execute(sql,(name,email,city))
    con.commit()
    print("data inserted successfully")
insert()   
def read():
    res=con.cursor ()
    sql="select * from user"
    res.execute(sql) 
    result=res.fetchall()
    print(result)
read()       


