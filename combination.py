def factorial(n):
    if n<0:
       return "invalid input"
    elif n==0 or n==1:
      return 1
    else:
     return n*factorial(n-1)
n=int(input("emter a number"))
r=int(input("emter a snumber"))
sum=factorial(n)//(factorial(r)*factorial(n-r))
print(sum)