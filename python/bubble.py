lst = list('swethasubramanian')

def bubble_sort(lst):
    l = len(lst)
    passes=0
    while passes < len(lst):
        for i,x in enumerate(lst[:-1]):
            if lst[i] > lst[i+1]:
                lst[i] = lst[i+1]
                lst[i+1] = x
        passes+=1

#    return ''.join(lst)

def bubble_sort2(l):
    for i, num in enumerate(l):
        try:
            if l[i+1] < num:
                l[i] = l[i+1]
                l[i+1] = num
                bubble_sort2(l)
                break
        except IndexError:
            pass
    return l

def selection_sort(lst):

    passes = 0
    length = len(lst)
    countind = length - 1

    while passes < length:
        maxval = lst[0]
        maxind = 0
        countind = length - passes - 1
        for i,x in enumerate(lst):
            if x > maxval and i < countind:
                maxind = i
                maxval = x
        lst[maxind] = lst[countind]
        lst[countind] = maxval
        print "Swapping {},{}".format(maxval,lst[maxind])
        passes += 1

    return lst

def insertion_sort(lst):

    for i in range(len(lst)):
        c = lst[i]
        pos = i

        while pos > 0 and lst[pos-1] > c:
            lst[pos] = lst[pos-1]
            pos -= 1

        lst[pos] = c

    return lst

def merge_sort(lst):

    if len(lst) > 1:
        s = int(len(lst) / 2)
        h1 = lst[:s]
        h2 = lst[s:]

        merge_sort(h1)
        merge_sort(h2)

        i,j,k = 0,0,0

        while i < len(h1) and j < len(h2):
            if h1[i] < h2[j]:
                lst[k] = h1[i]
                i += 1
            else:
                lst[k] = h2[j]
                j += 1
            k += 1

        while i < len(h1):
            lst[k] = h1[i]
            i += 1
            k += 1

        while j < len(h2):
            lst[k] = h2[j]
            j += 1
            k += 1

    return lst

print merge_sort(lst)
