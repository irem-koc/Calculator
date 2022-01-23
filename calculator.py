# for this project I wanna create a calculation machine!
# this app takes an input and return anything what you want!

print("Nice to see you there, welcome to our application!")
print("*****************************************************\n")
print("""
Welcome to my project!
1- If you wanna sum two object press 1
2- If you wanna abstract two object press 2
3- If you wanna product two object press 3
4- If you wanna divide two object press 1
5- If you wanna send afeedback press 0
6- If you wanna quit from application press 'q' :(
""")
def sum(x, y):
    return x+y

def difference(x, y):
    return x-y

def product(x, y):
    return x*y

def divide(x, y):
    return x/y

while True:
    a = input("Please enter a number what about you want... ")
    name = input("Please enter your name if you want? ")
    if a =="0":
        feedback = input("Oohh okay! Please tell us about our strengths or weaknesses ora any suggestion about our application?  ")
    elif a =="1":
        first = int(input("First number: "))
        second = int(input("Second number: "))
        print(sum(first, second))
    elif a =="2":
        first = int(input("First number: "))
        second = int(input("Second number: "))
        print(difference(first, second))
    elif a=="3":
        first = int(input("First number: "))
        second = int(input("Second number: "))
        print(product(first, second))
    elif a=="4":
        first = int(input("First number: "))
        second = int(input("Second number: "))
        print(divide(first, second))
    elif a=="q":
        print("See you later {}".format(name))
        break
    else:
        print("Enter a valid input!! ")
