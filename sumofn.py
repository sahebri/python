def fact(n):
    if(n<0):
        print("Not possible")
    elif n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

n=int(input("Enter a number"))
r=int(input("Enter a number"))
sum=0

sum=fact(n)//(fact(r)*fact(n-r))
print(sum)
