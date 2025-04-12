print("Hello, World!")
print ("empro")
x = 4
y = 3
print(x+y)
x = float(3)

print(x)
y = int(5)

print(y)
z = str(9)

print(z)
x = 7

print(type(x))
x = 5j

print(x)
print(type(x))

x = 3
print(type(x))

x = 8
print(float(x))

x = 8,3,4,5,6,7,8
print(set(x))

x = 1, 3, 5
print(frozenset(x))

x = 8
print(bytes(x))

x = 8
print(bool(x))

x = 8 > 3
print(bool(x))

x = 8 < 3
print(bool(x))

x = 7
print(range(x))

x = ("hello world")
print(x[4])

for y in "apple":
 print(y) 

 x = "empro rex"
 print(len(x))

 item={
    "brand" :"toyota",
    "model" :"prrado",
    "year" : 2015,
    "color" :'red'
 }
 print(item)

##get keys
 item={
    "brand" :"toyota",
    "model" :"prrado",
    "year" : 2015,
    "color" :'red'
 }
 x=item.keys()
 print(x)

#get item
#get value
 item={
    "brand" :"toyota",
    "model" :"prrado",
    "year" : 2015,
    "color" :'red'
 }
 x = item.items()
 print(x)

 #if ealse statement
 # 1 if statement
 a = 33
 b = 100
 if b > a:
   print("naso we talk ham")

   # 2 elif
   x = 10
   y = 10

   if y > x:
      print("x is geater than y")
   elif x == y:
      print("x is equal to y")

      # 3 else
   x = 100
   y = 10

   if y > x:
      print("x is less than y")
   elif x == y:
      print("x is equal to y")
   else:
    print("y is greater than x")

    #for loop
    #break statement
   fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break

   #continue statement
fruits = ["apple", "banana", "cherry","watermelon"]
for x in fruits:
   if x == "banana":
    continue
print(x) 

#the range function
for x in range(10):
  print(x)
#ddddd
  for x in range(2, 6):
   print(x)

   #Else in For Loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")

  
  print("PYHTON FUNCTIONS")
  #function
  def fun(fname):
   print(fname + " Refsnes")

fun("Emil")
fun("Tobias")
fun("Linus")


a =" phython lambda"
print(a.upper())

#example 1
x = lambda a: a + 10
print(x(5))

#2
x = lambda a, b: a * b
print(x(10, 5))

#3
x = lambda a, b, c: a + b + c
print(x(5, 6, 7))

a = "python array"
print(a.upper())

cars = ["Ford", "Volvo", "BMW"]

print(cars)


#import mod
#mod.greeting("empro")

import mod

a = mod.person1["name"]
print(a)

import datetime

x = datetime.datetime.now()
print(x)

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))


import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%B"))

import datetime

x = datetime.datetime.now()

print(x.strftime("%B"))

import math
x = math.ceil(1.4)
print(x)

import math

x = math.pi

print(x)

import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])


import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

import re

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")


username = input("Enter username:")
print("Username is: " + username)

import os
os.rmdir("youtube")