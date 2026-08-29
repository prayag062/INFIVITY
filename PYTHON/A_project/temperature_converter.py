def c_to_k(c):
    k=c+273.15
    return (f"{k} Kelvin")
    
def k_to_c(k):
    c= k-273.15
    return (f"{c} celcius")

def f_to_c(f):
    c= (f-32)*(5/9)
    return (f"{c} celcius")


def c_to_f(c):
    f= c(9/5)+32
    return (f"{f} farhenheit")

def f_to_k(f):
    k= (f-32)*(5/9)+273.15
    return (f"{k} Kelvin")
    

def k_to_f(k):
    f= (k-273.150)*(9/5)+32
    return (f"{f} farhenheit")





def main():
    while True:
        option=int(input('''
            Choose any option:
                1. celcius to kelvin
                2. kelvin to celcius
                3. farhenheit to celcius
                4. celcius to farhenheit
                5. farhenhrit to kelvin
                6. kelvin to farhenheit
        Your Choice: '''))

        if(option==1):
            celcius = float(input("celcius= "))
            print(f"Answer is {c_to_k(celcius)}")

        elif(option==2):
            kelvin= float(input("kelvin= "))
            print(f"Answer is {k_to_c(kelvin)}")

        elif(option==3):
            farhenheit = float(input("farhenheit= "))
            print(f"Answer is {f_to_c(farhenheit)}")

        elif(option==4):
            farhenheit = float(input("farhenheit= "))
            print(f"Answer is {c_to_f(farhenheit)}")

        elif(option==5):
            farhenheit = float(input("farhenheit= "))
            print(f"Answer is {f_to_k(farhenheit)}")

        elif(option==6):
            kelvin = float(input("kelvin= "))
            print(f"Answer is {k_to_f(kelvin)}")

        else:
            print("Invalid number")



if __name__ == "__main__":
    main()