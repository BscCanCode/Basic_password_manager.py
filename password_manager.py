print("Password_Manager")
print("Which Operation would you like to perform?")
print("1.Set_Password\n2.Enter_Password\n3.Change_Password\n4.Exit")
a=[] #mimics password storage

while True:
    try:
        n=int(input("Enter your choice: "))
        if n==4:
            print("Exit is success")
            break
        if 0<n<=3:
            if n==1:
                b=input("Set your password: ")
                a.append(b)
                print("Password is set successfully")
            elif n==2:
                if a:
                    c=input("Enter password to procees: ")
                    if c in a:
                        print("You can Proceed :D")
                    else:
                        print("Try Again,Password is incorrect")
                else:
                    print("To enter password,You should set it first")
            elif n==3:
                if a:
                    d=input("Are you sure you want to change password? yes/no: ")
                    if d=="yes":
                        e=input("Enter your previous password: ")
                        if e in a:
                            a.remove(e)
                            print("Password is Deleted,You can set new password:")
                            f=input("Enter your new password: ")
                            a.append(f)
                            print("New password set successfully")
                        else:
                            print("Incorrect input")
                    elif d=="no":
                        print("No password change")
                else:
                    print("To change password,you should have one")
            else:
                print("Enter yes/no")
        else:
            print("Enter your choice between 1-4")
    except:
        print("Enter proper input")
        
        
            
