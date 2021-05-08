import mysql.connector as con

#keep your sql server on and running
mydb = con.connect(host = "" , user = "" , passwd = "" )#enter host,user,passwd in all places through out the code


mycursor = mydb.cursor()

def show_dbs():
    mycursor.execute("show databases")
    for i in mycursor:
        print(i)    

def create_db(name_of_db):
    mycursor.execute("CREATE database {}".format(name_of_db))
    print("DATABASE CREATED")

def create_table(name_of_db,name_of_table):
    mydb_updated = con.connect(host = "" , user = "" , passwd = "" , database = str(name_of_db))
    mycursor = mydb_updated.cursor()
    mycursor.execute("CREATE TABLE {} (usernames VARCHAR(255), passwords VARCHAR(255), descriptions VARCHAR(255))".format(name_of_table))
    print("TABLE CREATED")
    
def inserting(name_of_db,name_of_table):
    mydb_updated = con.connect(host = "" , user = "" , passwd = "" , database = str(name_of_db))
    mycursor = mydb_updated.cursor()
    username = str(input("enter username\n"))
    password = str(input("enter password\n"))
    description = str(input("you can enter site name or app name the username and password belong too\n"))
    command = "INSERT INTO {} (usernames , passwords , descriptions ) VALUES (%s , %s , %s)".format(name_of_table)  
    val = (username,password,description)
    mycursor.execute(command,val)
    mydb_updated.commit()
    print("CREDENTIALS INSERTED")    

def show(name_of_db,name_of_table):
    mydb_updated = con.connect(host = "" , user = "" , passwd = "" , database = str(name_of_db))
    mycursor = mydb_updated.cursor()
    mycursor.execute("select * from {}".format(name_of_table))
    print("username followed by password followed by descriptiom")
    for i in mycursor:
        print(i)
    print("VALUES PRINTED") 
    
