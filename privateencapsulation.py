class BankAC:
    def __init__(self,ac_no,bal):
        self.ac_no=ac_no
        self.__bal=bal          #private member
    def get_bal(self):
        return self.__bal
    def set_bal(self,amount):
        if amount>0:
            self.__bal=amount
        else:
            print ("Negative cannot be used")

        
a=BankAC("123456",5000)
print(a.ac_no)
print(a.get_bal())
a.set_bal(500)
print(a.get_bal())