from itertools import tee
from os import system,name
import hashlib
import time 

UserStr = input("1)Md5 | 2)Exit \n\t")

if UserStr == '1':
    password = input("please enter string : ")
    text = bytes(password,'UTF-8')
    hashPass = hashlib.md5(text)
    print('your password will hash in : ')
    userWaiting = 3
    while userWaiting >= 0:
            print(userWaiting)
            userWaiting -= 1
            time.sleep(1)
            if name == "nt":
                system("cls")
            else:
                system("clear")
    print('*'*21)        
    print(f'Your Password Hashed : {hashPass.hexdigest()} ')    
    print('*'*21)     
elif UserStr == '2':
    print("Exiting . . .")
    time.sleep(2)
else:
    print("Not Valid input !")    
