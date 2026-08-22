def avg(a,b,c):
    avgerage = (a+b+c)/3
    return avgerage

# function call
num_1= float(input("Enter your first number : "))
num_2= float(input("Enter your second number : "))
num_3= float(input("Enter your third number : "))
print(f"Average of your numbers is {avg(num_1,num_2,num_3)}")