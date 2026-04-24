# An exception in Python is an occurrence that causes a disruption in the commands of the program while being executed. 
# When a Python code meets a condition that it cannot handle the execution, it raises an exception. 
# An object in Python that describes an error is called an exception.
try:
    x=10
    y=0
    r=x/y
    print(r)
except ZeroDivisionError:
    print("Cannot divide by zero")


print("Hello")