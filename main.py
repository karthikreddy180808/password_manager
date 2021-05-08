import access
import sql as db 
import time

print("welcome to password manager\n")
access.entry()
flag = 1

#there is no switch case in python 3.9 
while(flag):
    n = int(input("1 -> show databases\n2 -> create a databse\n3 -> create a table of a respective database\n4 -> insert values into specific table of a database\n5 -> show creds of a table\n6 -> exit\n"))
    if(n == 1): db.show_dbs()
    if(n == 2): db.create_db(input("name of the database\n"))
    if(n == 3): db.create_table(input("name of the database\n"),input("name of the table\n"))
    if(n == 4): db.inserting(input("name of the database\n"),input("name of the table\n"))
    if(n == 5):
        access.entry()
        db.show(input("name of the databse\n"),input("name of the table\n"))
    if(n == 6): flag = 0

    time.sleep(1.5)

print("thanks for using password_manager,have a great day!")
