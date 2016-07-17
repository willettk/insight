class Node():

    def __init__(self,data=None,next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next_node(self):
        return self.next_node

    def set_next_node(self,new_node):
        self.next_node = new_node

class LinkedList():

    def __init__(self,head=None):
        self.head = head

    def insert(self,data):
        new_node=Node(data)
        new_node.set_next_node(self.head)
        self.head = new_node

    def size(self):
        s = 0
        current = self.head
        while current is not None:
            s += 1
            current = current.get_next_node()
        return s

    def search(self,val):

        # Step through list, stop if item found
        current = self.head
        while current is not None:
            if current.get_data() == val:
                return True
            current = current.get_next_node()
        return False

    def delete(self,val):

        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == val:
                found = True
            else:
                previous = current
                current = current.get_next_node()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            # If I deleted the head, reset the head
            self.head = current.get_next_node()
        else:
            previous.set_next_node(current.get_next_node())
        return False

    def invert(self):
        new = self.head
        last = None
        while new.get_next_node() is not None:
            # Update to the current node 
            current = new
            # Record the next pointer before overwriting
            new = current.get_next_node()
            # Replace the old pointer with the new one
            current.set_next_node(last)
            # Remember what the new pointer will be
            last = current

        # Finally, if we've gone the whole way through, we need to set a new head
        new.set_next_node(last)
        self.head = new

    def print_list(self):
        current = self.head
        while current.get_next_node() is not None:
            print current.get_data()
            current = current.get_next_node()
        print current.get_data()
        print ''

    def get_head(self):
        return self.head

# Testing

mylist = LinkedList()
for data in range(5):
    mylist.insert(data)

mylist.print_list()
mylist.invert()
mylist.print_list()
mylist.delete(2)
mylist.print_list()
mylist.invert()
mylist.print_list()

