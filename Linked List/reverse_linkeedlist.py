from linkeed_lists import LinkeedList, DoublyLinkeedList

from typing import Optional

def reverseList(l_list) -> Optional[LinkeedList]:


    reversed_list = LinkeedList()

    while l_list.head:
        next_node = l_list.head.next
        l_list.head.next = reversed_list.head
        reversed_list.head = l_list.head
        l_list.head = next_node

    return reversed_list

ll = LinkeedList()
ll.add(2)
ll.add(4)
ll.add(8)
ll.add(16)
ll.add(32)

ll.print_all()
r = reverseList(ll)
r.print_all()
