import possiblesolutoins as ps
from random import randint


ALPHABET = "abcdefghijklmnopqrstuvwxyz"

global valueCount

valueCount = {}

#initializes valueCount to 0
for letter in ALPHABET:
    valueCount[letter] = 0

#finds the count of all the letters
for word in (ps.possibleSolutions):
    for letter in word:
        valueCount[letter] += 1

# for letter in ALPHABET:
#     print(letter, ":", valueCount[letter])

def solve(known = "?????", where=[], previousWord="crane", pos=ps.possibleSolutions):
    if (where == ["g", "g", "g", "g", "g"]):
        print("Well done")
        return 0, [0], True
    pos.remove(previousWord)

    notAllowed = []

    for position,result in enumerate(where):
        if (result == "g"):
            notAllowed.append(previousWord[position])
    

    for letter in notAllowed:
        for word in pos:
            if (letter in word):
                pos.remove(word)


    for position,result in enumerate(where):
        if (result == "r"):
            corLet = previousWord[position]
            tmpPos = []
            for word in pos:
                if (word[position] == corLet):
                    tmpPos.append(word)
            pos=tmpPos
        elif (result == "y"):
            corLet = previousWord[position]
            tmpPos = []
            for word in pos:
                if ((corLet in word) and (word[position] != corLet)):
                    tmpPos.append(word)
            pos=tmpPos

   #one day will change the randomness here to statistics based on the previously computed statistics
    return pos[randint(0, len(pos)-1)], pos, False


totalPossibilities = ps.possibleSolutions

solved = False
knownWord = "?????"
prevWord = "crane"
print("As a first word open with crane")
for i in range(5):
    vals = input("Input the different colours you got (g = grey / r = green / y = yellow)").split()
    
    prevWord, totalPossibilities, solved = solve(knownWord, vals, prevWord, totalPossibilities)
    if (solved == True):
        print("Let's gooooo")
        break
    print(f"Guess {prevWord}")
    
