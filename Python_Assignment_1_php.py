print("Hello, what do you want to do today") #Requests for the user's decision
print("Press a for addition")
print("Press s for subtraction")
print("Press m for multiplication")
print("Press d for division")

x = input(str()) #Stores user's input

first_value = float(input("Please enter the first value for your operation:"))#Requests user to input first value
second_value = float(input("Please enter the second value for your operation:"))#Requests user to input second value

#Performs the calculation to print out the answer
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