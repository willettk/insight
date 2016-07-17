class String:
    def __init__(self,val,next):
        self.val = val
        self.next = next

    def reverse(self,string):
        temp = string.next
        curr = string
        curr.next = None
        while temp is not None:
            future = temp.next
            temp.next = curr
            curr = temp
            temp = future
        return curr

    def __repr__(self):
        
        if self.next is None:
            return self.val
        else:
            return self.val + self.next.__repr__()

val = 'qwerty'

string = None
chars = list(val)
for v in val:
    while True:
        try:
            string = String(chars.pop(),string)
        except:
            break

print string ' --> ', string.reverse(string)
