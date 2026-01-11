class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkeedList:
    def __init__(self):
        self.head = None
    
    def add(self, value) -> None:
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def pop(self) -> int:
        if not self.head: 
            raise IndexError("pop from empty linked list")

        removed_node_value = self.head.value
        self.head = self.head.next

        return removed_node_value

    def find(self, target) -> bool:
        node = self.head
        while node is not None:
            if node.value == target: return True
            node = node.next
        return False

    def print_all(self) -> None:
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

class DoublyLinkeedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_front(self, value) -> None:
        new_node = Node(value)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node

        self.head = new_node

    def add_back(self, value) -> None:
        new_node = Node(value)
        new_node.prev = self.tail
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node

        self.tail = new_node


    def pop_front(self) -> int:
        if not self.head: 
            raise IndexError("pop from empty doubly linked list")

        removed_node_value = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None

        return removed_node_value

    def pop_back(self) -> int:
        if not self.tail: 
            raise IndexError("pop from empty doubly linked list")

        removed_node_value = self.tail.value
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None

        return removed_node_value

    def find(self, target, backwards = False) -> bool:
        if not backwards:
            node = self.head
            while node is not None:
                if node.value == target: return True
                node = node.next
            return False

        elif backwards:
            node = self.tail
            while node is not None:
                if node.value == target: return True
                node = node.prev
            return False

    def print_all(self, backwards = False) -> None:
        if not backwards:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

        elif backwards:
            node = self.tail
            while node is not None:
                print(node.value)
                node = node.prev

