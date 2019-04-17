import random
Your_score = 0
My_score = 0
tie = 0
myList = ["Rock", "Paper", "Scissors"]
print("Do you want to play a game of Rock, Paper, Scissors? Yes or No")
Uinput = input(":")
while Your_score or My_score or tie != 10:
    if Uinput.lower() == ("yes"):
        print("What do you choose as your move?")
        choice = input(":")
        while choice.lower() != ("rock") and choice.lower() != ("scissors") and choice.lower() != ("paper"):
            print("please enter a valid answer: rock, paper, or scissors")
            choice = input(":")
        print("You choose " + choice)
        guess = random.choice(myList)
        if choice.lower() == ("rock") and guess.lower() == ("rock"):
            print("My guess is " + guess)
            print("There is a tie")
            tie = tie+1
            print("The score is You " + str(Your_score) + " Me " + str(My_score) + " Tie " + str(tie))
            print("Do you want to continue? Yes or No")
            Uinput = input(":")
        if choice.lower() == ("rock") and guess.lower() == ("paper"):
            print("My guess is " + guess)
            print("Paper beats Rock")
            My_score = My_score + 1
            print("The score is You " + str(Your_score) + " Me " + str(My_score) + " Tie " + str(tie))
            print("Do you want to continue? Yes or No")
            Uinput = input(":")
        if choice.lower() == ("rock") and guess.lower() == ("scissors"):
            print("My guess is " + guess)
            print("Rock beats Scissors")
            Your_score = Your_score+1
            print("The score is You " + str(Your_score) + " Me " + str(My_score) + " Tie " + str(tie))
            print("Do you want to continue? Yes or No")
            Uinput = input(":")
        if choice.lower() == ("paper") and guess.lower() == ("rock"):
            print("My guess is " + guess)
            print("Paper beats Rock")
            Your_score = Your_score+1
            print("The score is You " + str(Your_score) + " Me " + str(My_score) + " Tie " + str(tie))
            print("Do you want to continue? Yes or No")
            Uinput = input(":")
        if choice.lower() == ("paper") and guess.lower() == ("paper"):
            print("My guess is " + guess)
            print("There is a tie")
            tie = tie + 1
            print("The score is You " + str(Your_score) + " Me " + str(My_score) + " Tie " + str(tie))
            print("Do you want to continue? Yes or No")
            Uinput = input(":")
        if choice.lower() == ("paper") and guess.lower() == ("scissors"):
            print("My guess is " + guess)
            print("Scissors beats Paper")
            My_score=My_score+1
            print("The score is You " + str(Your_score) + " Me " + str(My_score) + " Tie " + str(tie))
            print("Do you want to continue? Yes or No")
            Uinput = input(":")
        if choice.lower() == ("scissors") and guess.lower() == ("rock"):
            print("My guess is " + guess)
            print("Rock beats Scissors")
            My_score = My_score + 1
            print("The score is You " + str(Your_score) + " Me " + str(My_score) + " Tie " + str(tie))
            print("Do you want to continue? Yes or No")
            Uinput = input(":")
        if choice.lower() == ("scissors") and guess.lower() == ("paper"):
            print("My guess is " + guess)
            print("Scissors beats Paper")
            Your_score = Your_score + 1
            print("The score is You " + str(Your_score) + " Me " + str(My_score) + " Tie " + str(tie))
            print("Do you want to continue? Yes or No")
            Uinput = input(":")
        if choice.lower() == ("paper") and guess.lower() == ("paper"):
            print("My guess is " + guess)
            print("There is a tie")
            tie = tie + 1
            print("The score is You " + str(Your_score) + " Me " + str(My_score) + " Tie " + str(tie))
            print("Do you want to continue? Yes or No")
            Uinput = input(":")
    if Uinput.lower() == ("no"):
      print("The final score was: You " + str(Your_score) + " Me " + str(My_score) + " Tie " + str(tie))
      print("Have a nice day")
      break
