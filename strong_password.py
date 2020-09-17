password=input("enter your password")
length=len(password)
for i in password:
    if length>=6 or length<=12 and "$" in password and 2 in password and "Z" in password:
        print(password,"strong password")
        break
    else:
        print(password,"weak password")
        break


