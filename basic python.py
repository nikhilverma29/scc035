print("Hello World")\
# _____________________________________________________________________________
name = "Aice"
age = 25
height = 5.6
is_student = True
print(name,age,height,is_student)
# _____________________________________________________________________________
name = input("Enter Your Name:")
print("Hello, " + name + "!")
# _____________________________________________________________________________
num=int(input("Enter a number:"))
if num > 0:
    print("Positive number")
elif num<0:
    print("Negaive Number")
else:
    print("Zero")
# _____________________________________________________________________________
for i in range (5):
    print(i)
# _____________________________________________________________________________
count = 0
while count < 5:
    print(count)
count += 1
# _____________________________________________________________________________
def greet(name):
    return "Hello" + name + "!"
print(greet("Alice"))
# _____________________________________________________________________________
person = {"name":"Alice", "Age":25, "City":"New York"}
print(person["name"])
# _____________________________________________________________________________
class Person:
    def __init__(self, name, age):  
        self.name = name
        self.age = age
    def greet(self): 
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    p = Person("Alice", 25)     
    print(p.greet())  
# _____________________________________________________________________________
def calculator():
    num1 = float(input("Enter first number: "))
    operator = input("Enter an operator (+, -, /, *): ")
    num2 = float(input("Enter second number: "))

    if operator == '+':
        print("Result:", num1 + num2)
    elif operator == '-':
        print("Result:", num1 - num2)
    elif operator == '*':
        print("Result:", num1 * num2)
    elif operator == '/':
        if num2 != 0:  
            print("Result:", num1 / num2)
        else:
            print("Cannot divide by zero.")
    else:
        print("Invalid operator.")
    calculator()
# _____________________________________________________________________________
tasks = []  
def add_task(task):
    
    tasks.append(task)

def remove_task(task):
    
        tasks.remove(task)
        else:
        print("Task not found.")

def show_tasks():
    
    if not tasks:
        print("To-do list is empty.")
    else:
        print("To-do list:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")  
def main():
    
    while True:
        choice = input("Choose: add/remove/show/quit: ").lower()
        
        if choice == "add":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "remove":
            task = input("Enter task to remove: ")
            remove_task(task)
        elif choice == "show":
            show_tasks()
        elif choice == "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter add, remove, show, or quit.")


main()
