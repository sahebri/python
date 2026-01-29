class animal:
    def sound(self):
        print("Hi!!")
class dog(animal):
    def bark(self):
        print("barking")
class cat(animal):
    def meow(self):
        print("meowing")
c=cat()
c.meow()
c.sound()
d=dog()
d.bark()