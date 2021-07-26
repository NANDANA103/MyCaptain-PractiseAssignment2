#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Employee details stored in lists data structure
kirk = ["James Kirk", 34, "Captain", 2265]
spock = ["Spock", 35, "Science Officer", 2254]
mccoy = ["Leonard McCoy", "Chief Medical Officer", 2266]


# In[2]:


#Simple class example
class Dog:
    pass     #pass keyword is used as a placeholder indicating where code will eventually go.


# In[4]:


#Updated Dog class with an .__init__() method that creates name and age attributes
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# In[5]:


#Updated Dog class with class and instance attributes
class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):  #name and age are instance attributes
        self.name = name
        self.age = age


# In[11]:


#Object creation of Dog class 
Dog("Bruno",1)


# In[12]:


Dog("Shero",2)


# In[8]:


#Code showing that 2 different objects of the same class are different from each other
a = Dog("Shero",2)
b = Dog("Bruno",1)
a == b


# In[13]:


# Accessing Instance attributes using (.) dot notation
a = Dog("Shero",2)
b = Dog("Bruno",1)
print(a.name," ",a.age)
print(b.name," ",b.age)


# In[14]:


# Accessing Class attributes in the same manner
access = a.species
print(access)


# In[18]:


# How to change/update values of instance and class attributes
b.age = 4
print(b.age)
b.species = "Golden Retreiver"
print(b.species)


# In[29]:


# Creating instance Methods
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

    
# Accessing instance Methods to see output
a = Dog("Shero",2)
a.description()
b = Dog("Bruno",4)
b.description()
a.speak("Woof Woof")
b.speak("Bow Wow")


# In[26]:


# Displaying List elements
names = ["Fletcher", "David", "Dan"]
print(names)


# In[27]:


# See what happens when we print a object of Dog class
print(a)


# In[30]:


class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):           #__init__() is called as dunder method
        self.name = name 
        self.age = age

    # Replace .description() with __str__()
    def __str__(self):                       #__str__() is also called as dunder method
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
a = Dog("Shero",2)
print(a)
b = Dog("Bruno",4)
print(b)


# In[35]:


# Creating a new "Car" class with attributes and methods
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    def display(self):
        print(f"The {self.color} car has {self.mileage:,} miles")
        
blue = Car("blue",20000)
red = Car("red",30000)
blue.display()
red.display()


# In[37]:


# Modified Dog class with new attribute
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
a = Dog("Shero",2,"Golden Retriever")
b = Dog("Bruno",4,"German Shepherd")
miles = Dog("Miles", 4, "Bulldog")
buddy = Dog("Buddy", 9, "Dachshund")

dog1 = a.speak("Vow vow")
dog2 = b.speak("Bow Bow")
dog3 = miles.speak("Woof")
dog4 = buddy.speak("Yap")
print(dog1)
print(dog2)
print(dog3)
print(dog4)


# In[56]:


# Code to show Inheritance
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):           #__init__() is called as dunder method
        self.name = name 
        self.age = age

    # Replace .description() with __str__()
    def __str__(self):                       #__str__() is also called as dunder method
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
class GoldenRetreiver(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)

class GermanShepherd(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)   #access the parent class method from inside a method of a child class by using super()

class Bulldog(Dog):
    pass
class Dachshund(Dog):
    pass

a = GoldenRetreiver("Shero",2)
b = GermanShepherd("Bruno",4)
miles = Bulldog("Miles", 4)
buddy = Dachshund("Buddy", 9)

p = miles.species
q = buddy.name
print(p)
print(q)
print(b)
print(" ")
r = a.speak()
print(r)
s = b.speak()
print(s)


# In[46]:


# To determine which class a given object belongs to.
type(b)


# In[49]:


# To determine if miles is also an instance of the Dog class
isinstance(miles, Dog)

