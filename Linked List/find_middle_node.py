from linkeed_lists import LinkeedList, Node
from typing import Optional

def middle_node(l_list) -> Optional[Node]:
    head = l_list
    ahead = head.next

    while ahead and ahead.next:
        head = head.next
        ahead = ahead.next.next
       
    return head

