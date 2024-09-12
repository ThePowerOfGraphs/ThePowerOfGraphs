#importing the time module.
import time

#Welcome the player.
name = input("player name?")

print("Hello, " + name, "time to play hangman")

#Wait for a moment.
time.sleep(1)

print("Start guessing...")
time.sleep(0.5)

#Here the word is set to 'Secret'.
word = "secret"

#this are letters guessed, for now empty.
guesses = ''

#here we set the amount of turns.
turns = 10

#here i make a while loop that checks if turns is larger than zero
while turns > 0:
    #Here i make a counter that starts with zero.
    failed = 0
    #for ever character in the secret word.
    for char in word:
        #see if it is in the players guesse.
        if char in guesses:
            #then print out that character.
            print (char,end="")
        else:
            #if not found, print a dash.
            print ("-",end="")
            #and increase the failed counter by one.
            failed += 1
        #if failed is equalt to zero
    if failed == 0:
        #print you won
        print (" you won")
        #exit the script.
        break
    #ask the player to guesse a character
    guess = input("Guess a character!")
    #guess is added to guesses
    guesses += guess
    #if the guessed character is not in the word.
    if guess not in word:
        #A turn is spent.
        turns -= 1
        #and they are informed as such.
        print ("Wrong!")
        #they are told how many turns they have left.
        print ("You have", + turns, 'more guesses' )
        #if they are out of guesses.
        if turns == 0:
            #inform them of that.
            print("you lose.")
