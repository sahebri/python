class Bird:
    def move(self):
        print("......")
class Fish:
    def move(self):
        print("_____")
animals=[Bird(),Fish()]
for i in animals:
    i.move()        