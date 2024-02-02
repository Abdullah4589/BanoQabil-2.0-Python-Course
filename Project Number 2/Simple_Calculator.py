# Define Functions for operation to perform
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y!=0:
        return x/y
    else:
        return "Can't Divide by zero!"
# Providing Available options to user
print("Select Operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Asking User Choice
choice=input("Enter your choice(1,2,3,4):")

#Using Nested if/elif and else for asking user choice and perform relevant operation

if choice in("1","2","3","4"):
    num1=float(input("Enter First Number: "))
    num2=float(input("Enter Second Number: "))

    if choice=="1":
        print(f"{num1} + {num2} = {add(num1,num2)}")
    elif choice=="2":
        print(f"{num1} - {num2} = {subtract(num1,num2)}")
    elif choice=="3":
        print(f"{num1} * {num2} = {multiply(num1,num2)}")
    elif choice=="4":
        print(f"{num1} / {num2} = {divide(num1,num2)}")
    else:
        print("Invalid Input")
        




        

