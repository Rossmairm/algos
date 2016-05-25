#!/usr/bin/env python3

class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
    def size(self):
        current = self.head
        count = 0
        while current:
            count +=1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True

            else:
                current = current.get_next()
            if current is None:
                raise ValueError("Nothing there")
            return current
    def delete(self, data):
        current = self.head
        found= False
        while current and found is False:
            if current.get_data() == data:
                found = True

            else:
                previous = current
                current = current.get_next()
        if current is None:
             raise ValueError("Not found")
        if previous is None:
             self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


def main():
    action=LinkedList()
    while True:
        print ("What whould you like to do? \n 1. View List \n 2. Delete from list \n 3. Add to list \n 4. Search list \n 5. Exit")
        try:
            option=int(raw_input('Enter an option:'))
        except ValueError:
            print "Thats not a valid option"
        if option is 1:
            print("lol no")
        elif option is 2:
            del_data=raw_input('Which entry would you like to delete\n')
            action.delete(del_data)
        elif  option is 3:
            add_data=raw_input('What would you like to add\n')
            action.insert(add_data)
        elif option is 4:
            search_data=raw_input('What are you looking for\n')
            print(action.search(search_data))
        elif option is 5:
            exit()
        else:
            print("invaild entry")
if __name__=="__main__":
    main()
