class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_list_iterative(head):
    current = head

    while current is not None:
        print(current.val)
        current = current.next

    return

def print_list_recursive(head):
    current = head

    if current is None:
        return

    print(current.val)
    print_list_recursive(current.next)


# Driver code
a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d

print_list_iterative(a)
print_list_recursive(a)