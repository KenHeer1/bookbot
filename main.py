wordsstr = " words found in the document" 



def checkKey(dic, key):
    if key in dic.keys():
        return True
    else: 
        return False

def countWords (text):
    return len(text.split())

def countLetters (text):
    letterDict = {}

    for _letter in text:
        letter = _letter.lower()

        if letter.isalpha():
            if checkKey(letterDict, letter):
                letterDict[letter] = letterDict.get(letter) + 1
            else:
                letterDict[letter] = 1

    myKeys = list(letterDict.keys())
    myKeys.sort()
    sortedLetterDict = {i: letterDict[i] for i in myKeys}

    return sortedLetterDict

    




with open("books/frankenstein.txt") as f:
    print("--- Begin report of books/frankenstein.txt ---")    

    file_contents = f.read()
    print(str(countWords(file_contents)) + wordsstr) 

    print(" ")

    report = countLetters(file_contents)

    for letter in report.keys():
        print("The '" + letter + "' character was found " + str(report[letter]) + " times")



