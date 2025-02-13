#!/usr/bin/env python3
def happy_new_year():
    for num in range(10, 0, -1):  # Countdown from 10 to 1
        print(str(num))  
    print("Happy New Year!")


    # Call the function
happy_new_year()

def square_integers(numbers):
    return [x ** 2 for x in numbers]

print(square_integers([1, 2, 3, 4, 5]))  


def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
fizzbuzz()

