A = {'name':'A','stack':[2,1]}
B = {'name':'B','stack':[]}
C = {'name':'C','stack':[]}

def moveDisk(fromPile,toPile):

    fromStack = fromPile['stack']
    toStack = toPile['stack']
    disk = fromStack.pop()
    
    if len(toStack) > 0:
        temp = toStack.pop()
        if disk > temp:
            raise Exception("Cannot move a larger disk onto a smaller one.")
        else:
            toStack.append(temp)
            toStack.append(disk)
    else:
        toStack.append(disk)

    print "Moved {} from {} to {}".format(disk,fromPile['name'],toPile['name'])
    printStacks()

def moveTower(height,fromPile,toPile,withPile):

    if height > 0:
        moveTower(height-1,fromPile,withPile,toPile)
        moveDisk(fromPile,toPile)
        moveTower(height-1,withPile,toPile,fromPile)

def printStacks():

    print "A: ",A['stack']
    print "B: ",B['stack']
    print "C: ",C['stack']
    print ""

def testMoves():
    
    printStacks()
    moveDisk(A,C)
    
    printStacks()
    moveDisk(C,B)
    
    printStacks()
    moveDisk(A,C)
    
    printStacks()
    moveDisk(B,C)
    
    printStacks()

printStacks()
moveTower(len(A['stack']),A,C,B)
