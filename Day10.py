inputString = open("Input/Day 10.txt", "r").read().splitlines()
syntaxPairs = {"[":"]","{":"}","(":")","<":">"}

def solveBoth():    
    errorScore, autoCompleteScores, characterValues = 0, [], {')':3,']':57,'}':1197,'>':25137}
    for line in inputString:
        reducedString = reduceString(line)
        while len(reducedString) < len(line):
            line = reducedString
            reducedString = reduceString(line)
        if any(char in line for char in syntaxPairs.values()): #corrupt
            errorChar = [x for x in line if x in syntaxPairs.values()][0]
            errorScore += characterValues[errorChar]
        else: #incomplete
            autoCompleteScores.append(determineAutocompleteScore(line))
    print(errorScore)
    autoCompleteScores.sort()
    print(autoCompleteScores[int((len(autoCompleteScores)-1)/2)])

def reduceString(line):
    return line.replace("[]","").replace("{}","").replace("()","").replace("<>","")

def determineAutocompleteScore(line):
    reversedLine, characterValues, score = [syntaxPairs[x] for x in list(line[::-1])], {')':1,']':2,'}':3,'>':4}, 0
    for char in reversedLine:
        score = score * 5 + characterValues[char]
    return score

solveBoth()