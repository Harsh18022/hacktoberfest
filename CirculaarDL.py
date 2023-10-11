class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            last_node = self.head.prev
            last_node.next = new_node
            new_node.next = self.head
            new_node.prev = last_node
            self.head.prev = new_node

    def display(self):
        if not self.head:
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print()

# Example usage:
cdll = CircularDoublyLinkedList()
cdll.append(1)
cdll.append(2)
cdll.append(3)

cdll.display()
