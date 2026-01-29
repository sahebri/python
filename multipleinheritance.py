class cal1:
    def summ(self,a,b):
        return a+b
class cal2:
    def multi(self,a,b):
        return a*b
class divide(cal1,cal2):
    def divide(self,a,b):
        return a/b
d=divide()
print(d.summ(5,3))