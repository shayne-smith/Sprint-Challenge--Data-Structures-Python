import time

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare the input value with the value of the Node
        # if value < Node's value
        if value < self.value:
            # we need to go left
            # if we see that there is no left child,
                if self.left is None:
                    # then we can wrap the
                    # value in a BSTNode and park it
                    self.left = BSTNode(value)
                # otherwise there is a child
                else:            
                    # call the left child's insert method
                    self.left.insert(value)
        # otherwise, value >= Node's value
        else:
            # we need to go this Node's right child
            # if we see there is no right child, 
            if self.right is None:
                # then we can wrap the
                # value in a BSTNode and park it
                self.right = BSTNode(value)
            # otherwise there is a child
            else:
                # call the right child's insert method
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # compare the target value with the value of the Node
        # if target < Node's value
        if target < self.value:
            # we need to go left
            # if we see that there is no left child,
            if self.left is None:
                # return False
                return False
            # otherwise there is a child
            else:            
                # call the left child's contains method
                return self.left.contains(target)
        # otherwise, target > Node's value
        else:
            # if target is Node's value
            if target == self.value:
                return True
            # we need to go this Node's right child
            # if we see there is no right child, 
            if self.right is None:
                # return False
                return False
            # otherwise there is a child
            else:
                # call the right child's contains method
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):

        # max value will be on the right-most leaf
        # recursively iterate through BST via right node until max value is found
        if self.right is None:
            return self.value
        return self.right.get_max()
                
    # Call the function `fn` on the value of each noden
    # Pre-order BST traversal
    # O(n)
    def for_each(self, fn):

        # Base case is when a leaf is reached
        if self.value is None:
            return

        # run callback on current node
        fn(self.value)

        # run callback on left subtree
        if self.left is not None:
            self.left.for_each(fn)

        # run callback on right subtree
        if self.right is not None:
            self.right.for_each(fn)

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# Original runtime complexity is O(n^2)
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

bst2 = BSTNode(names_2[0])

for i in range(1, len(names_2)):
    bst2.insert(names_2[i])

for name_1 in names_1:
    if bst2.contains(name_1):
        duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
