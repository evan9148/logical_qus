num=int(input("enter your num"))
store = num
sum=0
while num>0:
    a=num%10
    sum=sum+a
    num=num//10
if store%sum==0:
    print("harshad")
else:
    print("not harshad")