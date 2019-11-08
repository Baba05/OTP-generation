import random
print("OTP GENERATION")
mail="ranjith@gmail.com"                #this contain taking input from user
password="12345"
umail=input("enter the Usermail:\n")
upass=input("enter Password:\n")


if(mail==umail)and(password==upass): #checking password and mail
    res=random.randrange(1000,9999)  #generating OTP for the first time and cheching
    print("UR OTP: ",res)
    check=int(input("Enter OTP\n"))       
    if(check==res):
        print("sucessfull Login")
    else:
        count=1
        while(count>=0):        #generating otp for nxt 2 times if user otp didnt match
            res=random.randrange(1000,9999)
            print("UR NEW OTP: ",res)
            check=int(input("enter new OTP\n"))
            if(check==res):
                print("sucessfull LOGIN")
                break
            count-=1
        else:
            print("login failed because of OTP TYPED WORNG")


else:
    print("invaild user or pass")
 
                
            
        

    
    
