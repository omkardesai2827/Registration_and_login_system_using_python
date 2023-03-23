import json 
import regex as re
import getpass as gt
def registration():
    while True:
        email=input("Enter your email id:")
        if "@" in email and "." in email:
            if len(email[:email.index("@")])>=4:
                if len(email[email.index("@"):email.index(".")])>=4:
                    if email[0] not in "1234567890" and email[0] not in "`~!@#$%^&*+-/":
                        break
        else:
            print("invalid email:start should be from a-z,'@' and '.' should be there and '@' and '.' not adjacent")
    while True:
        password=gt.getpass("Create a password")
        if 5<len(password)<16:
            special=re.findall("\W",password)
            if len(special)>=1:
                digit=re.findall("\d",password)
                if len(digit)>=1:
                    upper=0
                    for i in password:
                        if i.isupper()==True:
                            upper+=1
                    if upper>=1:
                        lower=0
                        for i in password:
                            if i.islower()==True:
                                lower+=1
                        if lower>=1:
                            break
        else:
            print("invalid password:there must be at least one speical character, uppercase,lowercase and digit")
    
    data["email"].append(email)
    data["password"].append(password)
    json_file=json.dumps(data,indent=4)
    a=open("email_password.json","w",encoding="utf-8")
    a.write(json_file)
    a.close()

def login():
    email=input("Enter your email id to login:")
    a=open("email_password.json","r",encoding="utf-8")
    dic=json.loads(a.read())
    count_email=0
    for i in dic["email"]:
        if i==email:
            count_email+=1
    if count_email==0:
        print("invalid email id not an existing account, register yourself")
    else:
        print("valid email id")
        password=input("Enter your password to login:")
        count_pass=0
        for i in dic["password"]:
            if i==password:
                count_pass+=1
        if count_pass==0:
            print("invalid password")
            fogot_password()
        else:
            print("valid password")
            print("you logged-in.")
    a.close()

def fogot_password():
    choose=input("you want to (a)retrieve your password or (b)change password:")
    a=open("email_password.json","r",encoding="utf-8")
    dic=json.loads(a.read())
    a.close()
    if choose=="a":
        email=input("write your email id:")
        for i in dic["email"]:
            if i==email:
                b=dic["email"].index(i)
        print("your password is :",dic["password"][b])
    else:
        email=input("write your email id:")
        new_password=gt.getpass("Create a new password:")
        for i in dic["email"]:
            if i==email:
                b=dic["email"].index(i)
        dic["password"][b]=new_password
        a=open("email_password.json","w",encoding="utf-8")
        json_file=json.dumps(dic,indent=2)
        a.write(json_file)
    a.close()
    
selection=input("If you are a new user register (A) and existing user login (B):")
if selection=="A":
    registration()
elif selection=="B":
    login()