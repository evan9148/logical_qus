string_list = ["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble", "Humble"]
i=0
a=[]
while i<len(string_list):
    if string_list[i] not in a:
        a.append(string_list[i])
    i=i+1
print(a)


# num=int(input("enter your num"))
# store=num
# i=2
# while i<=num:
#     value = store%10
#     if value%i==0:
#         print("not prime",value)
#         break
#     else:
#         print("prime",value)
#         sum=num//10
#     i=i+1

