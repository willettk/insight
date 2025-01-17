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
    for char in list(data):
        if not (char.isalpha() or char.isdigit() or char in ('-',' ')):
            dlist.remove(char)

    # Combine all legal characters back into a single string.
    dataStripped = ''.join(dlist)

    return dataStripped

def firstDashOnly(word):

    # Remove all dashes in a word unless there's a single example and it's at
    # the front of the string.

    nDashes = word.count('-')
    if nDashes > 1 and word[0] == '-':
        wordOneDashMax = (word[::-1]).replace('-','',nDashes-1)[::-1]
    else:
        wordOneDashMax = word

    return wordOneDashMax

def typeSort(data):

    # Split into words and numbers
    
    types,digits,letters = [],[],[]
    for word in data.split():

        wordNoDash = word.replace('-','')

        # Letters only
        if word.isalpha():
            letters.append(word)
            types.append(0)
        elif wordNoDash.isalpha():
            letters.append(wordNoDash)
            types.append(0)
        # Digits only
        else:
            wordDigit = firstDashOnly(word)
            try:
                wordAsInt = int(wordDigit)
                digits.append(int(wordAsInt))
                types.append(1)
            except ValueError:
                raise Exception("{} is neither a word nor a legal integer".format(word))

    # Sort the results for each type and put them in either end of a deque
    
    d = deque()
    for letter in sorted(letters,reverse=True):
        d.appendleft(letter)
    for digit in sorted(digits,reverse=True):
        d.append(digit)

    # Put the sorted results into the expected order of letters vs. digits
    
    result = [str(d.pop()) if t else d.popleft() for t in types]
    
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




