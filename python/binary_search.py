def isBadVersion(i,versions):
    
    if versions[i] == 0:
        return True
    else:
        return False

def logn_search(versions):
    upper = len(versions)
    lower = 0
    pivot = (lower + upper)//2
    while pivot != lower:
      print lower,pivot,upper
      if isBadVersion(versions[pivot],versions):
          print "Found it"
          lower = pivot
      else:
          upper = pivot# + 1
      pivot = (lower + upper)//2
    return pivot
