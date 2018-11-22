from random import randint
#imports a random number for the die roll
print("Do you want to play a game? Y or N ")
uInput = input(":")
if uInput.lower() == "y":
    print("This game is a guessing game.")
    print("You will be guessing what number the dice will roll")
    print("Please enter in what difficulty you want to play on: ");
    uInput = input()
    if(uInput.lower() == "easy"):
        Easy()
    elif(uInput.lower() == "medium"):
        Medium()
    else:
        Hard()
else:
    print("Alright hope to see you soon")

def Easy():
    score = 0
    guess = 0
    dieRoll = 0
    turns = 0
    while score <= 10:
        print("This game is a guessing game.")
        print("You will be guessing what number the dice will roll")
        guess = input("Time to guess what the dice will be 1-6:")
        dieRoll = randint(1, 2)
        print (dieRoll)
        print(guess)
    #you guess the right number and score goes up
        if int(guess) == dieRoll:
            print ("Congrats you won round 1 of 10") #will always print out round 1 of 10 when the round should be going up with each turn
            print ("You are at a score of " + str(score + 1))# score stays at 1 when it should be going up
            print ("You are at " + str(turns + 1) + " turns.") #turns stays at 1 and should be going up with each turn
            score += 1
            turns += 1
    #you guess the wrong number
        else:
            print("So close try again")
            print(score)
            print ("You are at a score of ", str(score))
            print ("You are at " + str(turns) + " turns.")
    #Ends the game if you have a score of 10
        if score == 10:
            print ("You have won the game in " + str(turns) + " turns")
            print ("You have earned a score of " + str(score))
            break
        else:
            print ("Do you want to play again? Y or N ")
            uInput = input(":")
            if(uInput.lower() == "y"):
                continue
            else:
                break

def Medium():
    score = 0
    guess = 0
    dieRoll1 = 0
    dieRoll2 = 0
    turns = 0
    while score <= 10:
        print("This game is a guessing game.")
        print("You will be guessing what number the dice will roll")
        guess = input("Time to guess what the dice will be 1-12:")
        dieRoll1 = randint(1, 6)
        dieRoll2 = randint(1,6)
        print (dieRoll1, dieRoll2, "Total of dice rolls is {}".format(dieRoll1 + dieRoll2))
        print(guess)
    #you guess the right number and score goes up
        if int(guess) == (dieRoll1 + dieRoll2):
            print ("Congrats you won round 1 of 10") #will always print out round 1 of 10 when the round should be going up with each turn
            print ("You are at a score of " + str(score + 1))# score stays at 1 when it should be going up
            print ("You are at " + str(turns + 1) + " turns.") #turns stays at 1 and should be going up with each turn
            score += 1
            turns += 1
    #you guess the wrong number
        else:
            print("So close try again")
            print(score)
            print ("You are at a score of ", str(score))
            print ("You are at " + str(turns) + " turns.")
    #Ends the game if you have a score of 10
        if score == 10:
            print ("You have won the game in " + str(turns) + " turns")
            print ("You have earned a score of " + str(score))
            break
        else:
            print ("Do you want to play again? Y or N ")
            uInput = input(":")
            if(uInput.lower() == "y"):
                continue
            else:
                break

def Hard():
    score = 0
    guess = 0
    dieRoll1 = 0
    dieRoll2 = 0
    dieRoll3 = 0
    turns = 0
    while score <= 10:
        print("This game is a guessing game.")
        print("You will be guessing what number the dice will roll")
        guess = input("Time to guess what the dice will be 1-18:")
        dieRoll1 = randint(1, 6)
        dieRoll2 = randint(1, 6)
        dieRoll3 = randint(1, 6)
        print (dieRoll1, dieRoll2, dieRoll3, "Total of dice rolls is: {}".format(dieRoll1 + dieRoll2 + dieRoll3)) #Appends it to the location at the {}
        print(guess)
    #you guess the right number and score goes up
        if int(guess) == (dieRoll1 + dieRoll2 + dieRoll3)):
            print ("Congrats you won round 1 of 10") #will always print out round 1 of 10 when the round should be going up with each turn
            print ("You are at a score of " + str(score + 1))# score stays at 1 when it should be going up
            print ("You are at " + str(turns + 1) + " turns.") #turns stays at 1 and should be going up with each turn
            score += 1
            turns += 1
    #you guess the wrong number
        else:
            print("So close try again")
            print(score)
            print ("You are at a score of ", str(score))
            print ("You are at " + str(turns) + " turns.")
    #Ends the game if you have a score of 10
        if score == 10:
            print ("You have won the game in " + str(turns) + " turns")
            print ("You have earned a score of " + str(score))
            break
        else:
            print ("Do you want to play again? Y or N ")
            uInput = input(":")
            if(uInput.lower() == "y"):
                continue
            else:
                break
