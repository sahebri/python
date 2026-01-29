class animal:
    def speak(self):
        print("Hello")
class dog(animal):
    def bark(self):
        print("Hi")
class babydog(dog):
    def weeps(self):
        print("weeping")
d=babydog()
d.weeps()
d.bark()
d.speak()
