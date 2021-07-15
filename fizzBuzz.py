# fizzBuzz.py

 #if a number is a multiple of 3, print Fizz
 #if a number is a multiple of 5, print Buzz
 #if a number is a multiple of both, print FizzBuzz
 
import math

for i in range(0,50):  
    if math.fmod(i, 15) == 0:
        print("FizzBuzz")
    elif math.fmod(i, 3) == 0:
        print("Fizz")
    elif math.fmod(i, 5) == 0:
        print("Buzz")
    else:
        print(i)