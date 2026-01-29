def fact(n):
    if(n==1):
        return 1
    else:
        f=1
        for i in range(1, n+1):
            f=f*i
        return f

n=int(input("Enter a number"))
temp=n
sum=0
while (n>0):
    r=n%10
    sum=sum+fact(r)
    n=n//10
if(temp==sum):
    print("Krishnamurthy")
else:
    print("not")

