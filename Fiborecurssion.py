def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
n=int(input("Enter the number"))
if(n<=0):
    print("Not possible")
else:
    for i in range(n):
        print(fibo(i))