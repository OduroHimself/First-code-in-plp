print("Hello, what do you want to do today")
print("Press a for addition")
print("Press s for subtraction")
print("Press m for multiplication")
print("Press d for division")

x = input(str())

first_value = float(input("Please enter the first value for your operation:"))
second_value = float(input("Please enter the second value for your operation:"))


if x ==  "a":
    y = first_value + second_value
    print("Your answer is: ", y)
elif x == "s":
    y = first_value - second_value
    print("Your answer is:", y)
elif x == "m":
    y = first_value * second_value
    print("Your answer is:", y)
elif x == "d":
    y = first_value / second_value
    print("Your answer is:", y)