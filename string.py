t="Hello "
s="world"
print(t[0])
print(t[3])
print(t[0:3])
print(t[::-1])
print(t[2:])
print(len(t))
f=t+"  "+s
print(f)
q=t*4
print(q)
print(t.upper())
print(s.lower())


name=" priya "
age=19
city="Uttarpara"
print(f'{name} is a {age} years old girl living in {city}')
print(name.find("a"))
print(name.replace("a","A"))
print(name.count("a"))
print(name.startswith("p"))
print(name.endswith("a"))
print(name.strip())
print(name.title())
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.swapcase())
del name
print(name)