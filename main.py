#Terminal Based Wordle

#Import libraries
import random, sys, re, colorama 
from colorama import Fore


#Create a user input processing function
def userInptProcess(userInput):
    return list(userInput)

#create an answer check function
def answerCheck(answer, userInp, userInpList):
    for i in range(len(userInpList)):
        if userInpList[i] == answer[i]:
            print(Fore.GREEN + userInp[i], end="" + Fore.WHITE)
        elif userInpList[i] in answer:
            print(Fore.YELLOW + userInpList[i], end="" + Fore.WHITE)
        else:
            print(userInpList[i], end="")
    
    if userInp == answer:
        print("\n" + "correct guess")
        return True
        

#Function that loads data
def loadData(data):
    # Read file as a string
    fileref = open(data, "r")
    textData = fileref.read()
    fileref.close()
    # Split text by one or more whitespace characters
    return re.split('\n', textData)


def main():
    #Variable that stores answer list
    answerList = loadData("database.txt")
    #stores current
    currentAnswer = random.choice(answerList)
    print(currentAnswer)

    

    userInput = input("Enter a five letter word: ").lower()
    inputArray = userInptProcess(userInput)
    
    gameLoop = answerCheck(currentAnswer, userInput, inputArray)

    while not gameLoop:
            userInput = input("\nEnter a five letter word: ").lower()
            inputArray = userInptProcess(userInput)
            if answerCheck(currentAnswer, userInput, inputArray):
                break
            

    

main()
