import sys
from collections import deque

def readFile(filename):

    # Load data; format should be a single line which will be loaded as a string
    
    with open(filename,'r') as f:
        data = f.readline().strip()

    return data

def removeOddChars(data):

    # Remove anything that's not a letter, digit, -, or <space> from string.
    # Assume we don't have to worry about mixed letter/digit words.
   
    dlist = list(data)
    for char in dlist:
        if not (char.isalpha() or char.isdigit() or char in ('-',' ')):
            dlist.remove(char)

    # Combine all legal characters back into a single string.
    dataStripped = ''.join(dlist)

    return dataStripped

def typeSort(data):

    # Split into words and numbers
    
    types,digits,letters = [],[],[]
    for word in data.split():
        # Letters only
        if word.isalpha():
            letters.append(word)
            types.append(0)
        # Digits only
        elif (word[0] == '-' and word[1:].isdigit()) or word.isdigit():
            digits.append(word)
            types.append(1)
        # Something else
        else:
            raise Exception("{} is neither a word nor a legal integer".format(word))

    # Sort the results for each type and put them in either end of a deque
    
    d = deque()
    for letter in sorted(letters,reverse=True):
        d.appendleft(letter)
    for digit in sorted(digits,reverse=True):
        d.append(digit)

    # Put the sorted results into the expected order of letters vs. digits
    
    result = [d.pop() if t else d.popleft() for t in types]
    
    # Final format is a string separated by <space>s
    
    sortedString = ' '.join(result)

    return sortedString

def writeFile(data,filename):
    
    with open(filename,'w') as f:
        print >> f,data

if __name__ == "__main__":
    
    # Run from command line
    
    try:
        data = readFile(sys.argv[1])
        lettersNumbersOnly = removeOddChars(data)
        sortedString = typeSort(lettersNumbersOnly)
        writeFile(sortedString,sys.argv[2])
    except IndexError:
        print "Usage:", "python cs_challenge.py <input_file> <output_file>"




