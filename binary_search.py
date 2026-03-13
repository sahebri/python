# mid = (low+high)/2  
# Here, the low is 0 and the high is 7.  
# mid = (0+7)/2  
# mid = 3 (Integer)  

def binary_search(list1, n):
    low=0
    high=len(list1)-1
    mid=0
    while low<=high:
        mid=(high+low)//2
        if list1[mid]<n:
            low=mid+1
        elif list1[mid]>n:
            high=mid-1
        else:
            return mid
    return -1
list1=[12,24,32,39,45,50,54]
n=50
result=binary_search(list1, n)
if result==-1:
    print("Element is not present")
else:
    print("Element is present at index", str(result))
