[1,1,0,0]
[1,1,1,1]
[0,0,0,0]
[]

def easy_soln(lst):
    idx = 0
    while idx < len(lst) - 1:
        for x in lst:
            if x == 0:
                return idx
            else:
                idx += 1
    return None

for lst in ([1,1,0,0],[1,1,1,1],[0,0,0,0],[]):
    print easy_soln(lst)
