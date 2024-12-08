# -*- coding: utf-8 -*-
"""Assessment.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/github/yatheeshpateel/ReBIT/blob/main/ReBIT/Assessment.ipynb

## Question 1
#### Define a class called Vehicle. Include attributes like make, model, and year. Add an initialization method to set these attributes
## Question 2
#### Add a method called display_info to the Vehicle class that prints out the vehicle’s information in a nicely formatted string.
"""

class Vehicle:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year


    def d(self):
        return f"vehicles information\n make: {self.make}\n model : {self.model}\n year :{self.year}"

make = input("enter the making information")
model = input("enter the model")
year = input("enter the year")

res = Vehicle(make,model,year)
print(res.d())

"""## Question 3
#### Create a subclass of Vehicle called Car that includes additional attributes like doors and engine_type. Override the display_info method to include these new attributes.
## Question 4
#### Write a method in the Car class to start_engine. This method should print a message that says the engine is starting, using the engine_type in the message.
"""

class Car(Vehicle):
    def __init__(self, make, model, year, doors, engine_type):
        super().__init__(make, model, year)
        self.doors = doors
        self.engine_type = engine_type

    def d(self):
        return (f"{super().d()}\nDoors: {self.doors}\nEngine Type: {self.engine_type}")

# Question 4
# Write a method in the Car class to start_engine. This method should print a message that says the engine is starting, using the engine_type in the message.

    def start_engine(self):
        print(f"The {self.engine_type} engine is starting")


make = input("enter the making information")
model = input("enter the model")
year = input("enter the year")
doors = input("Enter the number of doors: ")
engine_type = input("Enter the engine type: ")
c = Car(make, model, year, doors, engine_type)
print(c.d())
c.start_engine()

"""## Question 5
#### Implement a Bicycle subclass that inherits from Vehicle. Include additional attributes such as gear_count and bicycle_type.
"""

class Bicycle(Vehicle):
    def __init__(self,make,model,year,gear_count,bicycle_type):
        super().__init__(make,model,year)
        self.gear_count = gear_count
        self.bicycle_type = bicycle_type

"""# Question 6
# Create a Python class Circle. Use the __init__ method to set the radius and a method to calculate the area (use pi value from the math module).
"""

import math
class Circle:
    def __init__(self,r):
        self.r = r

    def calculate(self):
        return f"the area of the circle is {math.pi * self.r ** 2}"
r = float(input("enter the radius of circle"))
c = Circle(r)
c.calculate()

"""## Question 7
### Define a class Rectangle with attributes length and width. Include methods to calculate the area and perimeter.
"""

class Rectangle():
    def __init__(self,l,w):
        self.l = l
        self.w = w
    def area(self):
        return f"the area of a rectangle is {self.l * self.w}"

    def perimeter(self):
        return f"the perimeter of a rectangle is {2 *(self.l + self.w)}"

l = int(input("length"))
w = int(input("width"))
r = Rectangle(l,w)
print(r.area())
print(r.perimeter())

"""# Question 8 & 9
## Create a class Employee with properties name and employee_id. Include a method to print an email address, assuming it's employee_id@company.com. Extend the Employee class with a subclass Manager that has an additional attribute department and a method to print department details.

"""

class Employee:
    def __init__(self,name,eid):
        self.name = name
        self.eid = eid

    def email(slef):
        return f"{eid}@ReBIT.com"
class Manager(Employee):
    def __init__(self,name,eid,dept):
        super().__init__(name,eid)
        self.dept = dept

    def deptdetails(self):
        return f"department details :{self.dept}"

name = input("enter the name")
eid = input("enter the id")
e = Employee(name,eid)
print(e.email())
dept = input("enter the dprt")
m = Manager(name,eid,dept)
m.deptdetails()

"""## Question 10
#### Define a class ComplexNumber to represent complex numbers. Include methods to add and multiply two complex numbers.
"""

class ComplexNumber:

    def __init__(self,real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self,other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self,other):
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imag_part = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real_part, imag_part)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i" if self.imaginary >= 0 else f"{self.real} - {-self.imaginary}i"

comp1 = ComplexNumber(3,4)
comp2 = ComplexNumber(1,2)
sum_result = comp1 + comp2
print(f"sum result : {sum_result}")
multi_result = comp1 * comp2
print(f"Multiplication result : {multi_result}")

"""## Question 11
#### Create a class Book with attributes title, author, and price. Add a method to apply a discount to the price and another to format the book details as a string.
"""

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def apply_discount(self, percentage):
        self.price -= self.price * (percentage / 100)

    def display(self):
        print(f"Title: {self.title}, Author: {self.author}, Price: {self.price}")

# Inputs for book details
title = input("Enter the book title: ")
author = input("Enter the author's name: ")
price = float(input("Enter the book price: "))

# Creating a Book object
book = Book(title, author, price)

# Apply discount
discount = float(input("Enter the discount percentage: "))
book.apply_discount(discount)

# Display book details
book.display()

"""## Question 12
Implement a class Flight that can keep track of airline, flight number, and the list of passengers (use passenger names).

"""

class Flight:

    def __init__(self,airline,flight_number):
        self.airline = airline
        self.flight_number = flight_number
        self.passanger = []

    def __str__(self):
        return f"Airline : {self.airline}\nFlight Number : {self.flight_number}"


flg = Flight('KINGFISHER',"KF-5511")
print(flg)

class Flight:

    def __init__(self,airline,flight_number):
        self.airline = airline
        self.flight_number = flight_number
        self.passanger = []

    def add_passanger(self,name):
        if name not in self.passanger:
            self.passanger.append(name)
            return "Passanger added successfully"

    def remove_passanger(self,name):
        if name in self.passanger:
            self.passanger.remove(name)
        else:
            return "Passanger removed successfully"

    def get_passanger(self):

        if len(self.passanger) == 0:
            return "No Passanger"
        else:
            print("List of passanger")
            for names in self.passanger:
                print(names)
            return "Success"
    def __str__(self):
        return f"Airline : {self.airline}\nFlight Number : {self.flight_number}"

# object
flg = Flight('Air India',"AI-5511")
print(flg)
 # get passanger0
print(flg.get_passanger())
print()
 # add passanger
flg.add_passanger("yatheesh")
flg.add_passanger("abhi")
flg.add_passanger("sujay")
flg.add_passanger("darshan")
print()
 # get passanger
print(flg.get_passanger())
print()
 # remove passanger
flg.remove_passanger("darshan")
print()
 # get passanger
print(flg.get_passanger())

"""## Question 14
#### Create a class Animal with an attribute species. Add a method make_sound that prints a generic sound.
#### Question 15
#### Subclass Animal with Dog and Cat classes. Override the make_sound method to print "Woof" for dogs and "Meow" for cats.
"""

class Animal:
    def __init__(self,species):
        self.species = species

    def make_sound(self):
        print("animal sounds")

class Dog(Animal):
    def make_sound(self):
        print("bow")
class Cat(Animal):
    def make_sound(self):
        print("meow")

animal = input("enter the animal").strip()

if animal.lower() == "dog":
    d = Dog("Dog")
    d.make_sound()
elif animal.lower() == "cat":
    c = Cat("Cat")
    c.make_sound()
else:
    print("unknown animal type")

"""## Question 16
#### Develop a class Calculator with methods for basic operations: add, subtract, multiply, and divide. Handle division by zero gracefully.
"""

class Calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        if b != 0:
            return a/b
        else:
            return "Error: Division by zero"
a = int(input("enter a number"))
b = int(input("enter a number"))
c = Calculator()
operation = input("enter the operation")
if operation == "add":
    print("Result: ",c.add(a,b))
elif operation == "sub":
    print("Result: ",c.sub(a,b))
elif operation == "mul":
    print("Result: ",c.mul(a,b))
elif operation == "div":
    print("Result: ",c.div(a,b))
else:
    print("invalid")

"""## Question 17
#### Create a class WeatherForecast that has a method to add a temperature reading and another method to get the average temperature.
"""

class WeatherForecast:
    def __init__(self):
        self.temp = []

    def add_temp(self,tempr):
        self.temp.append(tempr)

    def avg(self):
        if self.temp:
            return  sum(self.temp) / len(self.temp)
        else:
            return "no temperature recorded "

t = WeatherForecast()
while True:
    tempr = input("Enter a temperature (or 'done' to finish): ")
    if tempr.lower() == 'done':
        break
    t.add_temp(float(tempr))
print(t.avg())

"""## Question 18
#### Define a Polygon class with methods to calculate perimeter and area. This class should be designed to be subclassed by specific polygon types like triangles and squares.
"""

class Polygon:
    def __init__(self,*args):
        self.args = args

    def Perimeter(self):
        pass

    def area(self):
        pass

"""## Question 19
#### Implement a subclass of Polygon for Triangle. Use attributes for the sides and appropriate methods to compute area (using Heron's formula).

"""

import math
class Triangle(Polygon):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

# Inputs for triangle sides
a = float(input("Enter the first side of the triangle: "))
b = float(input("Enter the second side of the triangle: "))
c = float(input("Enter the third side of the triangle: "))

# Create Triangle object
triangle = Triangle(a, b, c)

print(f"Perimeter of the triangle: {triangle.perimeter()}")
print(f"Area of the triangle: {triangle.area():.2f}")

"""### Question 20
Write a Square subclass of Polygon with a method override for area calculation specific to squares.
"""

class Square(Polygon):

    def __init__(self,side):
        self.side = side

    def area(self):
        ar = self.side * self.side
        return f"Area of Square {ar}"

# object
side = int(input("enter the side "))
obj1 = Square(side)
print(obj1.area())

"""## Question 21
#### Create a class Timer that can be used to time operations in Python. Use the time module for tracking start and end times.
"""

import time

class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = time.time()
        print("Timer started...")

    def stop(self):
        self.end_time = time.time()
        print("Timer stopped.")

    def elapsed_time(self):
        if self.start_time is not None and self.end_time is not None:
            return self.end_time - self.start_time


t = Timer()
input("Press Enter to start the timer...")
t.start()

input("Press Enter to stop the timer...")
t.stop()
print(f"Elapsed time: {t.elapsed_time()} seconds")

"""# Question 22
Design a Queue class using lists. Implement methods for enqueue, dequeue, and viewing the queue.

"""

class Queue:

    def __init__(self):
        self.items = []

    def enque(self,element):
        self.items.append(element)
        print(f"element {element} added successfully")

    def deque(self):
        self.items.pop(0)
        print(f"element {self.items[0]} removed successfully")

    def display(self):
        if len(self.items) == 0:
            return "Empty list"
        else:
            return f"Queue Items: {self.items}"


# object
obj1 = Queue()
print(obj1.display())
obj1.enque(454)
obj1.enque(135)
obj1.enque(235)
obj1.deque()
obj1.enque(454)
print(obj1.display())

"""## Question 23
#### Create a class Stack with methods for pushing, popping, and checking the size of the stack
"""

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"{item} pushed onto the stack")

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return "Stack is empty."

    def size(self):
        return len(self.stack)

s = Stack()
while True:
    print("\n1. Push\n2. Pop\n3. Check Size\n4. Exit")
    choice = int(input("Choose an option: "))

    if choice == 1:
        item = input("Enter the item to push: ")
        s.push(item)
    elif choice == 2:
        print(f"Popped item: {s.pop()}")
    elif choice == 3:
        print(f"Stack size: {s.size()}")
    elif choice == 4:
        break
    else:
        print("Invalid choice!")

"""## Question 24
#### Develop a MusicPlayer class with methods to play, stop, and load music tracks (simulated with print statements).
"""

class MusicPlayer:

    def __init__(self,song_name):
        self.song_name = song_name

    def play(self):
        return f"Playing {self.song_name} song..."

    def stop(self):
        return f"Pausing song {self.song_name}"

    def loadMusic(self,new_song):
        return f"Playing new song {new_song}"

song_name = input("enter the song name")
song = MusicPlayer(song_name)
print(song.play())
print(song.stop())
print(song.loadMusic("kantara"))

"""## Question 25
#### Implement a Database class that simulates a simple database interaction with methods to connect, disconnect, and execute a query (simulated with print statements).

"""

class Database:
    def __init__(self):
        self.connected = False

    def connect(self):
        if not self.connected:
            self.connected = True
            print("Connected to the database.")
        else:
            print("Already connected.")

    def disconnect(self):
        if self.connected:
            self.connected = False
            print("Disconnected from the database.")
        else:
            print("No active connection to disconnect.")

    def execute_query(self, query):
        if self.connected:
            print(f"Executing query: {query}")
        else:
            print("Cannot execute query. No active database connection.")

# Create Database object
db = Database()

while True:
    print("\n1. Connect\n2. Disconnect\n3. Execute Query\n4. Exit")
    choice = int(input("Choose an option: "))

    if choice == 1:
        db.connect()
    elif choice == 2:
        db.disconnect()
    elif choice == 3:
        query = input("Enter your query: ")
        db.execute_query(query)
    elif choice == 4:
        break
    else:
        print("Invalid choice!")
