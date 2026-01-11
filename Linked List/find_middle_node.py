from linkeed_lists import LinkeedList, Node
from typing import Optional

def middleNode(l_list) -> Optional[Node]:
    head = l_list.head
    ahead = head

    while ahead and ahead.next:
        head = head.next
        ahead = ahead.next.next
       
    return head

