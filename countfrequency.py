list=[4,7, 8]
c=0
list2=[]
n=int(input("Enter the number of elements in the list."))
for i in range(1,n+1):
    i=int(input())
    list.append(i)
for j in list:
    if j not in list2:
        print(j, ":",list.count(j))
        list2.append(j)


