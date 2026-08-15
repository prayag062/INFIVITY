raw_input_fruit=input("Enter name of fruits seprated by comma(,) : ")

print(raw_input_fruit)

fruit_list=[item.strip() for item in raw_input_fruit.split(",")]

print(fruit_list)
