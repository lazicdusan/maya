#stuff collected from various sources intended for personal reminders

#unpacking
data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
name, shares, price, date = data
print (name) #prints first item
print (shares) #prints second
print (price)
print (date)

#unpacking with a star
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record #star is the final/rest stuff
print (name) #prints first item
print (email) #prints second
print (phone_numbers) #prints the rest

#star can be in the middle
grades = (1,2,3,4,5) 
first, *middle, last = grades #star is the middle
print (middle) #prints the middle items only

#count the most mentioned item in the list
from collections import Counter
words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
'my', 'eyes', "you're", 'under'
]
word_counts = Counter(words) 
top_three = word_counts.most_common(3) #gets top three results
print(top_three)

word_counts['not'] #counts how many times 'not' happens
word_counts['eyes'] #counts how many times 'eyes' happens

morewords = ['nja','sdfadsf','OOO']
word_counts.update(morewords) #add new stuff to word_counts

#list comprehensions

jaPunoVolimTijanu = [1,2,3,4,5,6,7,8,9,10000000000000000]

for t in jaPunoVolimTijanu:  #2
	print (t)                  #1   

COMPREHENSION = [print (t) for t in jaPunoVolimTijanu]

squares = []
for x in range(10):     #2
	squares.append(x**2)  #1

COMPREHENSION = squares = [x**2 for x in range(10)]

#list comprehensions with if
mylist = [1, 4, -5, 10, -7, 2, 3, -1]

for n in mylist:
	if n > 0:
		print (n)

COMPREHENSION = [n for n in mylist if n > 0]

for n in mylist: #2 
  if n > 0:      #3 
    print (n)    #1 

# Determine if any .py files exist in a directory
import os
dirname = 'D:\Dusan\Stvaralastvo\Skripte'
files = os.listdir(dirname)

if any(name.endswith('.py') for name in files): #endswith and startswith can be used to check stuff like this
	print('There be python!')
else:
	print('Sorry, no python.')

#str.find(), str.endswith(), str.startswith()
#startswith basic filtering
choices = ('http:', 'https:', 'ftp:')
url = 'http://www.python.org'
if url.startswith(choices):
	print ('yes sir')

text = 'yeah, but no, but yeah, but no, but yeah'
# Exact match
text == 'yeah'

# Match at start or end
text.startswith('yeah')

text.endswith('no')

# Search for the location of the first occurrence
text.find('no')

# search and replace
text.replace('yeah', 'yep')

#dictionaries reminder
c = {'y': 2, 'z': 4 }
print (len(c))
print (list(c.keys()))
print (list(c.values()))

#combining strings with join
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
' '.join(parts) #'Is Chicago Not Chicago?'
','.join(parts) #'Is,Chicago,Not,Chicago?'
''.join(parts) #'IsChicagoNotChicago?'

data = ['ACME', 50, 91.1]
','.join(str(d) for d in data) #'ACME,50,91.1'

#string combining and printing
print(a + ':' + b + ':' + c) # Ugly
print(':'.join([a, b, c])) # Still ugly
print(a, b, c, sep=':') # Better

#getting a random number value from a list
import random
values = [1, 2, 3, 4, 5, 6]
print (random.choice(values))

#decorator
def verbose(original_function): 
    # make a new function that prints a message when original_function starts and finishes
    def new_function(*args, **kwargs):
        print("Entering decorator like a baws", original_function.__name__)
        original_function(*args, **kwargs)
        print("Exiting decorator like a baws", original_function.__name__)
 
    return new_function

@verbose
def widget_func():
    # some code
    print ('this is going to work')

widget_func()

#make a class
class Employee:
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)


#This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
#This would create second object of Employee class"
emp2 = Employee("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()

#make a second class
class Namirnice:
    def __init__(self, ime, podgrupa, cena, rokTrajanja):
        self.ime = ime
        self.podgrupa = podgrupa
        self.cena = cena
        self.rokTrajanja = rokTrajanja
    #create the first function in the class
    def printajNamirnice(self):
        print ("Ime namirnice je", self.ime,"iz podgrupe", self.podgrupa, "," , "cena je:", self.cena, "evra")

    #crete the second function
    def printajRokoveTrajanja(self):
        print ("Rok trajanja za", self.ime, "je do", self.rokTrajanja)


#This would create first object the class"
namirnica01 = Namirnice("kupus", "povrce", 5, 2017)
#This would create second object of the class"
namirnica02 = Namirnice("mleko", "mlecni proizvod", 2, 2016)

#call the first function from the class
namirnica01.printajNamirnice()
#call the second function from the class
namirnica02.printajRokoveTrajanja()

#call both
namirnica01.printajNamirnice()
namirnica01.printajRokoveTrajanja()

#make a third class
#create a baseclass
class Animal(object):
  name = None

  def speak(self):
    print ("My name is ", self.name)

  def walk(self):
    print ("I don't know how to walk")

  def breathe(self):
    print ("I don't know how to breathe")

#create a subclass
class Dog(Animal):
  breed = None

  def speak(self):
    print ("Woof!!!")

  def walk(self):
    print ("I walk on 4 legs")

  #extend the functionality of the baseclass
  def what_is_breed(self):
    print (self.breed)

class Fish(Animal):

  #override the baseclass function
  def breathe(self):
    print ("I breathe underwater")

#test how the class works
fido = Dog()
fido.breed = "Doberman"
fido.what_is_breed()

dory = Fish()
dory.breathe()

#print all permutations or combinations in a list
from itertools import permutations
items = ['a', 'b', 'c']
#print only two
for p in permutations(items,2):
  print(p)

#write to the external file 
filename = "C:\\Users\\lazicdusan\\Desktop\\testFile.txt"
txt = open(filename, "a")
txt.write('this is written by python \n') #if \n doesn't work use os.linesep
txt.close()

#stop the cmd to not go away fast
input('da li volis Tijanu?')

#string formatting
print ("Hello my name is %s and i am %s" %('Dusan','30'))
print ("Hello my name is {} and i am {}".format('Dusan','30'))
print ("Hello my name is {0} and i am {1}".format('Dusan','30'))
print ("Hello my name is {user} and i am {age}".format(user='Dusan',age='30'))
podaci = ['Dusan',30]
print ("Hello my name is {} and i am {}".format(*podaci))