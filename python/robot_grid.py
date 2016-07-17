def backtrack(r, c):
  while r > 0 and c > 0:
    if (r == 0 & c == 0):
      return 1
    if (r > 0 | c > 0):
      return 0
 
  return backtrack(r+1, c) + backtrack(r, c+1)

print backtrack(2,2)
