import sys
import random
name = input("What is your name?\n")
def run():
    print(f"Hello,{name}, let's play hangman!")
    print("start guessing.....")

    #Defining the bag of words

    bag_of_words = ["Algorithm","Data structures","Artificial intelligence","Machine learning","Networking","Computer security","Cryptography","Computer architecture","Operating systems","Computer graphics","Distributed computing","Databases","Data mining","Software engineering","Theory of computation","parameters", "control", "exception", "nomalization"]
    word = random.choice(bag_of_words)
    guesses = " "
    turns = 10
    while turns > 0:
     failed = 0
    for char in word:
      if char in guesses:
        print(char)
      else:
        print("_")
        failed += 1
    if failed == 0:
      print("You win!")
      choice = input("Would you like to play again? y/n\n")
      if "y" in choice:
        run()
      elif "n" in choice:
        sys.exit()
      else:
        print("Something went wrong, type y or n.")
    guess = input("Guess a character:")
    guesses += guess
    if guess not in word:
      turns -= 1
      print("Wrong!")
      print(f"You have {turns} more guesses.")
      if turns == 0:
        print("You lose!")
        choice = input("Would you like to play again? y/n\n")
        if "y" in choice:
          run()
        elif "n" in choice:
          sys.exit()
        else:
          print("Something went wrong, type y or n.")

