import time

print("made by act4d2")
print("simple calculator program version 1.0.0")
problemformath = input("x = multiplication a = addition s = subtraction. choose one: ")

if problemformath == "a":
    print("you can use decimals for addition!")
    firstnumberaddition = input("first number to add: ")
    secondnumberaddition = input("second number to add: ")
    sumofaddition = float(firstnumberaddition) + float(secondnumberaddition)
    print("the sum of the two numbers you added is " + str(sumofaddition))
elif problemformath == "x":
    print("as of now you cannot use decimals for multiplication :( ")
    firstnumbermultiplication = input("first number to multiply: ")
    secondnumbermultiplication = input("second number to multiply: ")
    sumofmultiplication = int(firstnumbermultiplication) * int(secondnumbermultiplication)
    print("the sum of the two numbers you multiplied is " + str(sumofmultiplication))
elif problemformath == "s":
    print("you can use decimals for subtraction!")
    firstnumbersubtraction = input("first number to subtract: ")
    secondnumbersubtraction = input("second number to subtract: ")
    sumofsubtraction = float(firstnumbersubtraction) - float(secondnumbersubtraction)
    print("the sum of the two numbers you subtracted is " + str(sumofsubtraction))
else:
    print("you didn't choose a correct problem!")
retry = input("would you like to try a different problem? a for addition x for multiplication s for subtraction: ")
if retry == "a":
    print("you can use decimals for addition!")
    firstnumberaddition = input("first number to add: ")
    secondnumberaddition = input("second number to add: ")
    sumofaddition = float(firstnumberaddition) + float(secondnumberaddition)
    print("the sum of the two numbers you added is " + str(sumofaddition))
elif retry == "x":
    print("as of now you cannot use decimals for multiplication :( ")
    firstnumbermultiplication = input("first number to multiply: ")
    secondnumbermultiplication = input("second number to multiply: ")
    sumofmultiplication = int(firstnumbermultiplication) * int(secondnumbermultiplication)
    print("the sum of the two numbers you multiplied is " + str(sumofmultiplication))
elif retry == "s":
    print("you can use decimals for subtraction!")
    firstnumbersubtraction = input("first number to subtract: ")
    secondnumbersubtraction = input("second number to subtract: ")
    sumofsubtraction = float(firstnumbersubtraction) - float(secondnumbersubtraction)
    print("the sum of the two numbers you subtracted is " + str(sumofsubtraction))
else:
    print("you didn't choose a correct problem!")
    retry = 0
if retry == 0:
    print("have a good day")
    time.sleep(3)