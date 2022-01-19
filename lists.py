
class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

def has_cycle(head):
    slow = head
    fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            print(slow.value, fast.value)
            return True
    return False

def cycle_length(begin):
    curr = begin.next
    count = 1
    while curr != begin:
        curr = curr.next
        count += 1
    return count

def get_cycle_begin(head, L):
    ptr1 = head
    ptr2 = head
    for i in range(L):
        ptr1 = ptr1.next
    while ptr1 != ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    return ptr1.value

def cycle_begin(head):
    slow = head
    fast = head
    has_cycle = False
    L = 0
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast: #
            L = cycle_length(slow)
            has_cycle = True
            break
    if has_cycle:
        return get_cycle_begin(head, L)
    return None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3) # 3
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

print(has_cycle(head))
head.next.next.next.next.next.next = head.next.next
print(has_cycle(head))

print(cycle_begin(head)) # 3
