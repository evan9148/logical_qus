num_students=int(input("enter students number"))
expenses_students=int(input("enter expenses of a student"))
value=num_students*expenses_students
print(value)
if value<=50000:
    print("budget is under controll")
else:
    print("budget is out of under controll")

