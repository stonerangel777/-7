import math

try:
    number = int(input("Въведете цяло число: "))

    if number < 0:
        print("Invalid Number")
    else:
        result = math.sqrt(number)
        print("Квадратен корен:", result)

except ValueError:
    print("Invalid Number")

finally:
    print("Good Bye")