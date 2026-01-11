from linkeed_lists import LinkeedList
from find_middle_node import middle_node
from merge_two_lists import merge_two_lists

def mergesort(head):
    if not head or not head.next:
        return head

    middle = middle_node(head)
    after_middle = middle.next

    middle.next = None

    left = mergesort(head)
    right = mergesort(after_middle)

    sorted_list = merge_two_lists(left, right)

    return sorted_list



ll = LinkeedList()
ll.add(1)
ll.add(11)
ll.add(9)
ll.add(8)
ll.add(2)
ll.add(0)
ll.add(6)

test_mergesort(ll.head)

