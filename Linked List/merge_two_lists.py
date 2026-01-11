from linkeed_lists import Node

def merge_two_lists(list1, list2):
    dummy = Node(0)
    tail = dummy

    while list1 and list2:
        if list1.value <= list2.value:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    tail.next = list1 or list2# Either list1 or list2 will always be true, so this syntax captures the true value and assigns it to tail.next.
    
    return dummy.next # dumy.next because the list is initialized with an empty node