def find_max_min(lst):
    max_element = lst[0]
    min_element = lst[0]
    for element in lst:
        if element > max_element:
            max_element = element
        elif element < min_element:
            min_element = element
    return max_element, min_element

# Initial list1
lst = []

# number of elements as input
num = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, num):
    ele = int(input())
    # adding the element
    lst.append(ele)

max_element, min_element = find_max_min(lst)

print("Maximum element in the list is", max_element)
print("Minimum element in the list is", min_element)