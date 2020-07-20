class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):

        # if list is null or has only 1 node
        # just return the list as is
        if node is None or node.get_next() is None:
            self.head = node
            return node

        # recursively call reverse_list with next node until end of list is reached
        reversed_list = self.reverse_list(node.get_next(), node)

        # flip next_node pointers to reverse the list
        node.next_node.next_node = node

        return reversed_list
        
        
