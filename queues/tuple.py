names = ("Hawo","Halima","Abdirizack","Abdiaziz")
#Accessing an item in a Tupple
print(names[1])

#Adding an item to a tupple
names = ("Hawo","Halima","Abdirizack","Abdiaziz")
y = list(names)
y.append("sadia")
names = tuple(y)
print(names)

#Removing an item in a tupple
names = ("Hawo","Halima","Abdirizack","Abdiaziz")
x = list(names)
x.remove("Abdiaziz")
names = tuple(x)
print(names)