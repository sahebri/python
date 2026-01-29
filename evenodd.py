list=[]
n=int(input())
even=[]
odd=[]
for i in range(1, n+1):
    i=int(input())
    list.append(i)
for i in list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even numbers in list",even)
print("Odd number is list",odd)