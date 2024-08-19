import random
import math

lower_bound = int(input("Enter lower bound - "))
upper_bound = int(input("Enter upper bound - "))

x = random.randint(lower_bound, upper_bound)
total_guesses = math.ceil(math.log(upper_bound - lower_bound + 1, 2))
print(f"Total guesses you have - {total_guesses}")

count = 0
flag = False

while count < total_guesses:
    guess = int(input("Enter your guess - "))
    count += 1

    if guess == x:
        print(f"Congratulations! You guessed the number in {count} tries")
        flag = True
        break
    elif guess < x:
        print(f"Your guess too small try again! you have {total_guesses - count} chances")
    elif guess > x:
        print(f"Your guess too high try again! you have {total_guesses - count} chances")
    else:
        print(f"Try again! you have {total_guesses - count} chances")

if not flag:
    print(f"Sorry! You have exhausted all your chances. The number was {x} better luck next time")