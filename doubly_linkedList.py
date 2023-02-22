class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None  # New pointer to the previous node


class linked_list:
    def __init__(self):
        self.head = node()
        self.tail = node()  # New tail node

        # Set head's next to tail and tail's prev to head
        self.head.next = self.tail
        self.tail.prev = self.head

    def append(self, data):
        new_node = node(data)

        # Set the new node's prev to the current tail's prev
        new_node.prev = self.tail.prev
        # Set the current tail's prev's next to the new node
        self.tail.prev.next = new_node
        # Set the new node's next to the current tail
        new_node.next = self.tail
        # Set the current tail's prev to the new node
        self.tail.prev = new_node

    def length(self):
        current = self.head.next
        total = 0
        while current != self.tail:
            total += 1
            current = current.next
        return total

    def display(self):
        elements = []
        current_node = self.head.next
        while current_node != self.tail:
            elements.append(current_node.data)
            current_node = current_node.next
        print(elements)

    def get(self, index):
        if index >= self.length():
            print("Error: 'Get' index out of range!")
            return None
        current_index = 0
        current_node = self.head.next
        while True:
            if current_index == index:
                return current_node.data
            current_index += 1
            current_node = current_node.next

    def erase(self, index):
        if index >= self.length():
            print("Error: 'Erase' index out of range!")
            return
        current_index = 0
        current_node = self.head.next
        while True:
            if current_index == index:
                # Set the current node's prev's next to its next
                current_node.prev.next = current_node.next
                # Set the current node's next's prev to its prev
                current_node.next.prev = current_node.prev
                return
            current_index += 1
            current_node = current_node.next


def main():
    print("\n~~TESTS~~")
    my_list = linked_list()

    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    my_list.append(4)

    print("\nThe full linked list is: ")
    my_list.display()

    my_list.erase(1)

    print("\nThe appended linked list is: ")
    my_list.display()

    print("\nThe element at the second index is: " + str(my_list.get(2)))


if __name__ == '__main__':
    main()
