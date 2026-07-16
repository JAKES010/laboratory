import random

print("1. Start Game")
print("2. Exit")
print()
select = input("Choose an option from the menu:")
print()
if select == "2":
    leave = input("Type 'exit' to quit: ")
    if leave == "exit" :
     print("Goodbye!")
     exit()
print("\n" * 4)
print("------------------------------")
print("     Livour guessing game!")
print("------------------------------")
print()

print("[Guess the number of Goals and you get lunch on the house!]")
print()
mm_count = random.randint(1, 10)
attempt_limit = 5
attempts = 0

while attempts < attempt_limit:
    guess_text = input("How many Goals are in the jar?:\n-->")
    guess = int(guess_text)
    attempts += 1
    if attempts == attempt_limit : 
        print(f"Bye, you're done in {attempts} attempts!")
        break
    elif mm_count == guess:
        print()
        print(f"Congrats you got a free lunch! It was {guess}.")
        break
    elif guess < mm_count:
        print()
        print("Sorry, that's too LOW!")
    else :
        print("That's too HIGH!")