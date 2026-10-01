class Linked_List:
    
    class __Node:

# for def __init__(self, val):
# Big-O: O(1)
# Sets the node's value, prev, and next using a fixed number of steps.
        def __init__(self, val):
            self.val = val
            self.prev = None
            self.next = None    

 # for def __init__(self):
# Big-O: O(1)
# Creates the header and trailer and connects them using a fixed number of steps.
    def __init__(self):
        self.__header = Linked_List.__Node(None)
        self.__trailer = Linked_List.__Node(None)

        self.__header.next = self.__trailer
        self.__trailer.prev = self.__header

        self.__size = 0
    
# for def __len__(self):
# Big-O: O(1)
# Just returns the size that is already stored, so it does not have to go through the list.
    def __len__(self):
        return self.__size

# for def append_element(self, val):
# Big-O: O(1)
# Adds the new node right before the trailer using a fixed number of pointer changes.
    def append_element(self, val):
        new_node = Linked_List.__Node(val)
        previous_node = self.__trailer.prev

        new_node.prev = previous_node
        new_node.next = self.__trailer
        previous_node.next = new_node
        self.__trailer.prev = new_node
        self.__size += 1

# for def insert_element_at(self, val, index):
# Big-O: O(n)
# It may have to move through part of the list to find the index before inserting the new node.
    def insert_element_at(self, val, index):
        if index < 0 or index >= self.__size:
            raise IndexError

        new_node = Linked_List.__Node(val)

        if index < self.__size / 2:
            current = self.__header
            current_index = -1

            while current_index < index:
                current = current.next
                current_index += 1

        else:
            current = self.__trailer
            current_index = self.__size

            while current_index > index:
                current = current.prev
                current_index -= 1

        new_node.prev = current.prev
        new_node.next = current
        current.prev.next = new_node
        current.prev = new_node

        self.__size += 1

# for def remove_element_at(self, index):
# Big-O: O(n)
# It may have to move through part of the list to find the node before removing it.
    def remove_element_at(self, index):
        if index < 0 or index >= self.__size:
            raise IndexError

        if index < self.__size / 2:
            current = self.__header.next
            current_index = 0

            while current_index < index:
                current = current.next
                current_index += 1

        else:
            current = self.__trailer.prev
            current_index = self.__size - 1

            while current_index > index:
                current = current.prev
                current_index -= 1

        current.prev.next = current.next
        current.next.prev = current.prev

        self.__size -= 1

        return current.val

# for def get_element_at(self, index):
# Big-O: O(n)
# It may have to move through part of the list to find the value at the requested index.

    def get_element_at(self, index):
        if index < 0 or index >= self.__size:
            raise IndexError

        if index < self.__size / 2:
            current = self.__header.next
            current_index = 0

            while current_index < index:
                current = current.next
                current_index += 1

        else:
            current = self.__trailer.prev
            current_index = self.__size - 1

            while current_index > index:
                current = current.prev
                current_index -= 1

        return current.val

# for def rotate_left(self):
# Big-O: O(1)
# Moves the first node to the end by changing a fixed number of pointers.

    def rotate_left(self):
        if self.__size <= 1:
            return

        first = self.__header.next
        second = first.next
        last = self.__trailer.prev

        self.__header.next = second
        second.prev = self.__header

        last.next = first
        first.prev = last
        first.next = self.__trailer
        self.__trailer.prev = first

# for def __str__(self):
# Big-O: O(n^2)
# It goes through every node, but repeatedly adding onto the growing string can take more time as the string gets bigger.       
    def __str__(self):
        if self.__size == 0:
            return '[ ]'

        result = '[ '
        current = self.__header.next

        while current != self.__trailer:
            result = result + str(current.val)

            if current.next != self.__trailer:
                result = result + ', '

            current = current.next

        result = result + ' ]'
        return result

# for def __iter__(self):
# Big-O: O(1)
# Sets the iterator to start at the first actual node in the list.
    def __iter__(self):
        self.__iter__current = self.__header.next
        return self
    
# for def __next__(self):
# Big-O: O(1)
# Gets the current value and moves to the next node using one pointer.

    def __next__(self):
        if self.__iter__current == self.__trailer:
            raise StopIteration

        value = self.__iter__current.val
        self.__iter__current = self.__iter__current.next
        return value

# for def __reversed__(self):
# Big-O: O(n)
# Goes backward through every node once and adds each value to the new reversed list.


    def __reversed__(self):
        reversed_list = Linked_List()

        current = self.__trailer.prev

        while current != self.__header:
            reversed_list.append_element(current.val)
            current = current.prev

        return reversed_list

#some regular tests

if __name__ == '__main__':
    my_list = Linked_List()

    print("Empty:", my_list)

    my_list.append_element(1)
    my_list.append_element(2)
    my_list.append_element(3)

    print("After append:", my_list)
    print("Length:", len(my_list))

    print("Get index 0:", my_list.get_element_at(0))
    print("Get index 1:", my_list.get_element_at(1))
    print("Get index 2:", my_list.get_element_at(2))

    my_list.insert_element_at(4, 1)
    print("After inserting 4 at index 1:", my_list)

    removed = my_list.remove_element_at(3)
    print("Removed:", removed)
    print("After removal:", my_list)

    my_list.rotate_left()
    print("After rotate left:", my_list)

    print("For loop:")
    for value in my_list:
        print(value)

    print("Reversed:", reversed(my_list))




#trying indexes that are out of bounds to see if they raise IndexError
    print("Testing invalid indexes:")

    try:
        my_list.get_element_at(-1)
        print("ERROR: get_element_at(-1) should have raised IndexError")
    except IndexError:
        print("PASS: get_element_at(-1) raised IndexError")

    try:
        my_list.get_element_at(3)
        print("ERROR: get_element_at(3) should have raised IndexError")
    except IndexError:
        print("PASS: get_element_at(3) raised IndexError")

    try:
        my_list.remove_element_at(-1)
        print("ERROR: remove_element_at(-1) should have raised IndexError")
    except IndexError:
        print("PASS: remove_element_at(-1) raised IndexError")

    try:
        my_list.remove_element_at(3)
        print("ERROR: remove_element_at(3) should have raised IndexError")
    except IndexError:
        print("PASS: remove_element_at(3) raised IndexError")

    try:
        my_list.insert_element_at(99, -1)
        print("ERROR: insert_element_at(-1) should have raised IndexError")
    except IndexError:
        print("PASS: insert_element_at(-1) raised IndexError")

    try:
        my_list.insert_element_at(99, 3)
        print("ERROR: insert_element_at(3) should have raised IndexError")
    except IndexError:
        print("PASS: insert_element_at(3) raised IndexError")

    #tring some empty tests

    print("Testing empty list:")

    empty_list = Linked_List()

    print("Empty list:", empty_list)
    print("Length:", len(empty_list))

    try:
        empty_list.get_element_at(0)
        print("ERROR: get_element_at(0) should have raised IndexError")
    except IndexError:
        print("PASS: get_element_at(0) raised IndexError")

    try:
        empty_list.remove_element_at(0)
        print("ERROR: remove_element_at(0) should have raised IndexError")
    except IndexError:
        print("PASS: remove_element_at(0) raised IndexError")

    try:
        empty_list.insert_element_at(5, 0)
        print("ERROR: insert_element_at(0) should have raised IndexError")
    except IndexError:
        print("PASS: insert_element_at(0) raised IndexError")

    empty_list.rotate_left()
    print("After rotate left:", empty_list)

    print("Reversed empty list:", reversed(empty_list))

    #one element list

    print("Testing one-element list:")

    one_list = Linked_List()
    one_list.append_element(1)

    print("List:", one_list)
    print("Length:", len(one_list))
    print("Get index 0:", one_list.get_element_at(0))

    one_list.rotate_left()
    print("After rotate left:", one_list)

    print("Reversed:", reversed(one_list))

    print("For loop:")
    for value in one_list:
        print(value)