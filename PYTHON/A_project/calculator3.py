

#   Modules Function
def mod(a,b):
    modules=(a%b)
    return modules

#average function
def avg(a,b):
    average=(a+b)/2
    return average

# function call
num_1=int(input("Enter a number: "))
num_2=int(input("Enter the second number: "))
task=input("What do you want to find average(1) or module(2): ")
if(task==1):
    print(f"Average of your numbers is {avg(num_1,num_2)}")

elif task==2:
    print(f"Modules of your number is {mod(num_1,num_2)}")

else:
    print(f"Invalid input")