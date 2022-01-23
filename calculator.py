


# a = int(input("Enter 1st number: "))
# b = int(input("Enter 2nd number: "))
# print('''1.Addition
# 2.Subtraction
# 3.Multiplication 
# 4.Division''') 
# c = int(input("Choose anyone among 1, 2, 3, 4: "))
# if c == 1:
#     print(f"Addition is {a+b}")
# elif c == 2:
#     print(f"Subtraction is {a-b}")
# elif c == 3:
#     print(f"Multiplication is {a*b}")        
# else:
#     print(f"Division is {a/b}")





def add(a,b):
    return(a+b)

def subtract(a,b):
    return(a-b)

def multiple(a,b):
    return(a*b)

def divide(a,b):
    return(a/b)


num1=int(input("Enter the  first number :"))
num2=int(input("Enter the  second number :"))


print("select the option : ")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Exit")

while(True):
  choice=int(input("enter the choice from (1/2/3/4/5)"))
  if choice==1:
      print("Addition of two number,",num1,"and",num2,"is : ",add(num1,num2))
  elif choice==2:
      print("Subtraction of two number,",num1,"and",num2,"is : ",subtract(num1,num2))
  elif choice==3:
      print("Addition of two number,",num1,"and",num2,"is : ",multiple(num1,num2))
  elif choice==4:
      print("Addition of two number,",num1,"and",num2,"is : ",divide(num1,num2))
  elif choice==5:
      print("End of program")
      exit()
else:
    print("Invalid choice try again")