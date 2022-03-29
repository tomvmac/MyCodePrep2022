# Remove Duplicates From Linked List

# You're given the head of a Singly Linked List whose nodes are in sorted order with respect to their values.

# Write a function that returns a modified version of the Linked List that doesn't contain any nodes with
# duplicate values.  The Linked List should be modified in place, ie.  do not create a new linked list.
# Also the modified Linked List should still have its nodes sorted with respect to their values.

# Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to
# None / null if it's the tail of the list.

# Sample Input:
# linkedList = 1 -> 1 -> 3 -> 4 -> 4 -> 4 -> 5 -> 6 -> 6

# Sample Output:
# 1 -> 3 -> 4 -> 5 -> 6
import null as null

class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data}"

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append_val(self, x):
        '''add x to the end of the list'''

        if not isinstance(x, Node):
            x = Node(x)

        if self.head == None:
            self.head = x
        else:
            self.tail.next = x
        self.tail = x

    def removeDuplicatesFromLinkedList(self):

        # Initialize curr to head of list
        curr = self.head
        while curr is not None:
            # Iterate through all nodes until next is null
            # For each item, compare currNode and nextNode
            # if equal, set currNode.next to nextNode.next

            if curr.next is not None:
                if curr.data == curr.next.data:
                    curr.next = curr.next.next

            curr = curr.next

    def __str__(self):
        # [5->4->10->1]
        to_print = ""
        # iterate through list
        curr = self.head
        while curr is not None:
            to_print += str(curr.data) + "->"
            curr = curr.next

        if to_print:
            return "[" + to_print[:-2] + "]"
        else:
           return "[]0"




# Driver code
node1 = Node(1)
node2 = Node(1)
node3 = Node(3)
node4 = Node(4)
node5 = Node(4)
node6 = Node(6)

my_list = LinkedList()
my_list.append_val(node1)
my_list.append_val(node2)
my_list.append_val(node3)
my_list.append_val(node4)
my_list.append_val(node5)
my_list.append_val(node6)

print(my_list)

my_list.removeDuplicatesFromLinkedList()

print(my_list)
