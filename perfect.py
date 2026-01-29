n=int(input("Enter a number"))
temp=n
sum=0
for i in range(1,n):
    if(n%i==0):
        sum=sum+i
        print(i)
if(temp==sum):
    print("Perfect!!")
else:
    print("Not")