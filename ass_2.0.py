print("~~~~~~~~~~~ Functions   ~~~~~~~~~~~~")
# def key word is used to define function

def my_function():
    print("Hello From a function")


my_function()
# passing 1 Argument
print("Passing 1 Argument To The Function")


def my_function1(fname):
    print(fname + "Refsnes")


my_function1("Email")
my_function1("Tobias")
my_function1("Linus")
# passing 2 Argument to the function
print("Passing Two Arrgument to the Function ")


def my_function(fname, lname):
      print(fname + " " + lname)


my_function("Emil", "Refsnes")
# Arbitrary Arguments, *args


def my_function(*kids):
      print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
# Keyword Arguments



def my_function(child3, child2, child1):
      print("The youngest child is " + child3)


my_function(child1="Emil", child2="Tobias", child3="Linus")
# how many keyword arguments that will be passed into your function, add two asterisk: **


def my_function(**kid):
      print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Refsnes")
# Default parameter value


def my_function(country="Norway"):
      print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
# passing list as an argument


def my_function(food):
      for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# Function is  Returning Values


def my_function(x):
      return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))
# Recursive Function


def tri_recursion(k):
      if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
      else:
        result = 0
      return result

print("\n\nRecursion Example Results")
tri_recursion(9)
print("~~~~~~~~~~~ Dictionary ~~~~~~~~~~~~")
#Dictnary is a pair of Key Value pair
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#printing value by providing key
print(thisdict["brand"])
#Duplicates Not Allowed if we try to creat Duplicate it will update the value of it
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
#To find How many Items is in Dictnary use len()Function 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(len(thisdict))
#The values in dictionary items can be of any data type:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)
#we can acess dictnary value by get()  method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
#keys() method will return a list of all the keys in the dictionary.
x = thisdict.keys()
# values() method will return a list of all the values in the dictionary.
x = thisdict.values()
#items() method will return each item in a dictionary, as tuples in a list.
x = thisdict.items()
#we can update the values of Dictnary using update() method
thisdict.update({"year": 2020})
print(thisdict)
#Adding an item to the dictionary 
thisdict["color"] = "red"
print(thisdict)
#adding element using update method
thisdict.update({"color": "red"})
print(thisdict)
#Removing item using pop() method
thisdict.pop("model")
print(thisdict)
#popitem() is used to removing last element 
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
#del keyword used to delete dictionary completely

#clear() method is used to empties the dictnary 
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
print("~~~~~~~~~   Sets  ~~~~~~~~~~~~")
thisset = {"apple", "banana", "cherry"}
print(thisset)
#sets not allows Dupplicates
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
#len() function is used to find how many items is in set
print(len(thisset))
#sets allows all data types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)
#set() constructor is used to make a set 
thisset = set(("apple", "banana", "cherry"))
print(thisset)
#add method is use to add element in set 
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
#to add items from another set uodate() method is used
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
#To remove an item in a set, use the remove(), or the discard() method.
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
#to remove last element pop method is used
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
#clear() method is used to clear a set
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
#The del keyword will delete the set completely
#The union() method returns a new set with all items from both sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
#The intersection_update() method will keep only the items that are present in both sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)
#he symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)