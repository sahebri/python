class person:
    def info(self):
        print("I am a person")
class employee(person):
    def imp_info(self):
        print("I am an employee")
class student:
    def stu_info(self):
        print("I am a student")
class w_s(employee,student):
    def w_s_info(self):
        print("I study and work")
ws=w_s()
ws.info()
ws.imp_info()
ws.stu_info()
ws.w_s_info