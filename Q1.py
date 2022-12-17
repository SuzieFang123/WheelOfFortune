import random
import time
def chooseWord():
    validWords = ["generation", "consume", "computing", "residence", "memory", "hosting"]

    return validWords[random.randint(0,5)]

def printStringWithSpace(word):
        for x in word:
            print(x,sep=" ")
        print()
        print()

def convertToUnderscores(word):
    underscore = ""
    for num in range(0,len(word)):
        underscore += "_"
    return underscore

def updateWord(currentRep, word, letter):
    string = ""
    x = list(word)
    y = 0

    for z in currentRep:
        if letter == x[y]:
            string += letter
        elif z == x[y]:
            string += z
        else:
            string += "_"
        y += 1
    return string

def updateUsedLetters(usedLetters, letter):
    return(usedLetters + letter)

def main():
    usedLetters = ""  # no letters guessed yet
    wrongGuesses = 0  # keep track of incorrect guesses
    word = chooseWord()
    print("The word to guess is ", word)
    currentRep = convertToUnderscores(word)
    printStringWithSpace(currentRep)
    continueGame = True
    while continueGame:
        guess = input("Please enter a letter (a-z): ")
        # check for valid input
        while not (guess.isalpha()) or len(guess) != 1:
            guess = input("Please enter valid input(a single letter (a-z)):")
        guess = guess.lower()
        print("You have guessed ", guess)

        if guess in word:
            # letter is in the secret word so update the current representation
            currentRep = updateWord(currentRep, word, guess)
            printStringWithSpace(currentRep)
            if currentRep == word:
                print("You have guessed the right word.")
                continueGame = False

            else:
                wrongGuesses +=1
                print("Incorrect, please try again. Number of wrong tries: ",wrongGuesses,sep="")
                printStringWithSpace(currentRep)
                if wrongGuesses == 5:
                    continueGame = False
                    print("You have used up your five chances. Better luck next time")

        else:
            # letter has been guessed already -- update the user
            print("You have already guessed that letter!!!")
            time.sleep(1)
            print("Here are the letters you have guessed so far: ")
            printStringWithSpace(usedLetters)

    main()

