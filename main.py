
"""
Brute Force Demo  Password Risk Simulation
Author: Prendi
Created on: June 23, 2020

This script demonstrates how easily weak passwords can be cracked using brute-force logic.
It is intended for educational and ethical use only, to raise awareness about password security.
"""

from random import randint
import time
start_time = time.time()
user_pass = input("Enter your password: ")
combinations = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
    'u','v','w','x','y','z'
]
guess = ""
while guess != user_pass:
    guess = ""
    for letter in range(len(user_pass)):
        guess_letter = combinations[randint(0, 25)]
        guess = str(guess_letter) + str(guess)
    print(guess)
end_time = time.time()
elapsed = end_time - start_time

print(f"\nTime Taken: {elapsed:.2f} Seconds")
print("Your password is:", guess)
