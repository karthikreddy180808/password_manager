import hashlib

def entry():
    with open("" , "r") as f: #paste the text document path
        creds = f.readline()
        if(len(creds) == 0):
            with open("" , "w") as f: #even here paste the text document path
                password = str(input("give a master password\n"))
                hashedpass = hashlib.sha256(str.encode(password)).hexdigest()
                f.write(str(hashedpass))
            f.close()
            entry()
        else:
            masterpass = str(input("enter master password\n"))
            if (hashlib.sha256(str.encode(masterpass)).hexdigest() == creds):
               print("access granted")
            else:
               print("wrong master password")
               entry()
    f.close()

    
