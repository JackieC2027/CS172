# TO DO: ADD YOUR HEADER COMMENT HERE
# Programmer: Jackie Cheng
# Date 4/3/23
# Purpose: 
import random
def findMatches(word, letter):
    newWord = ""
    for eachLetter in range(len(word)):
        if word[eachLetter] == letter:
            newWord += letter
        else:
            newWord += "-"
    return newWord
    
def merge(word1, word2):
    newWord = ''
    for letter in range(len(word1)):
        if not word1[letter] == "-":
            newWord += word1[letter]
        elif not word2[letter] == "-":
            newWord += word2[letter]
        else:
            newWord += "-"
    return newWord
            
if __name__ == "__main__":
    # TO DO: WRITE THE MAIN ROUTINE HERE
    boolValue = False
    while not boolValue:
        try:
            userFile = input("Enter name of the data file: ")
            inFile = open(userFile, 'r')
            boolValue = True
        except Exception:
            print("Error: that file does not exist. Try again.")
    
    random.seed(15)
    wordList = []
    for line in inFile:
        wordList.append(line)
    wordChoice = random.choice(wordList).rstrip()
    
    print("I have a %d letter word, try to guess it." %len(wordChoice))
    print("You will enter one letter at the time.")
    
    emptyWord = "-" * len(wordChoice)
    counter = 0
    while emptyWord != wordChoice:
        userLetter = input("Enter a letter to see if it's in the word: ")
        if userLetter in wordChoice:
            print("%s is part of my secret word." %userLetter)
            possibleMatches = findMatches(wordChoice, userLetter)
            filledWord = merge(emptyWord, possibleMatches)
            print(filledWord)
            if filledWord == wordChoice:
                print("Congratulations, you guessed my secret word!")
                print("It took you %d turns to guess my secret word." %counter)
        else:
            print("%s is not in my secret word." %userLetter)
            print("Guess another letter.")
        counter += 1
            