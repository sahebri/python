def  fact(n):
    if (n<0):
        print ("Not possible")
    elif n==0:
        return 1
    else:
        return n*fact(n-1)
n=int(input("Enter the number"))
temp=n
sum =0
while (n>0):
    r=n%10
    sum=sum+fact(r)
    n=n//10
if(sum==temp):
    print("Krishnamutry")
else:
    print("Not")