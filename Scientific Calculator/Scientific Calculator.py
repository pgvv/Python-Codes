import math

while True:
    print(" \n Choose the math operation:\
            \n 0: Addition \
            \n 1: Subtraction \
            \n 2: Multiplication \
            \n 3: Division \
            \n 4: Modulo \
            \n 5: Raise to a power \
            \n 6: Logarithm \
            \n 7: Sine \
            \n 8: Cosine \
            \n 9: Tangent \
            \n 10: Square Root")
    
    oper= int(input("\n Your option: "))
    # Addition
    if oper == 0:
        val1= float(input("\n First value: "))
        val2= float(input("\n Second value: "))

        print("\n The result is " + str(val1 + val2))
    # Subtraction
    elif oper == 1:
        val1= float(input("\n First value: "))
        val2= float(input("\n Second value: "))

        print("\n The result is " + str(val1 - val2))
    # Multiplication
    elif oper == 2:
        val1= float(input("\n First value: "))
        val2= float(input("\n Second value: "))

        print("\n The result is " + str(val1 * val2))
    # Division
    elif oper == 3:
        val1= float(input("\n First value: "))
        val2= float(input("\n Second value: "))

        print("\n The result is " + str(val1 / val2))
    # Remainder
    elif oper == 4:
        val1= float(input("\n First value: "))
        val2= float(input("\n Second value: "))

        print("\n The result is " + str(val1 % val2))
    # Power
    elif oper == 5:
        val1= float(input("\n First value: "))
        val2= float(input("\n Second value: "))

        print("\n The result is " + str(math.pow(val1, val2)))
    # Logarithm
    elif oper == 6:
        val1= float(input("Value for calculating log to the base 2: "))

        print("\n The result is " + str(math.log(val1, 2)))
    # Sine
    elif oper == 7:
        val1= float(input("Value in degrees: "))

        print("\n The result is " + str(math.sin(math.radians(val1))))
    # Cosine
    elif oper == 8:
        val1= float(input("Value in degrees: "))

        print("\n The result is " + str(math.cos(math.radians(val1))))
    # Tangent
    elif oper == 9:
        val1= float(input("Value in degrees: "))

        print("\n The result is " + str(math.tan(math.radians(val1))))
    # Square Root
    elif oper == 10:
        val1= float(input("Value: "))

        print("\n The result is " + str(math.sqrt(val1)))
    # Handling invalid inputs
    else:
        print("\n Invalid option! Please try again")
        continue
    

    back= input("\n Go back to main menu? (y/n) ")
    if back== "y":
        continue
    else:
        break