from linkeed_lists import LinkeedList

def mergeTwoLists(list1, list2):
    curr_1 = list1
    curr_2 = list2

    new_list = LinkeedList()
    curr_nl = new_list

    while curr_1 and curr_2:
        if curr_1.val <= curr_2.val:
            curr_nl.next = curr_1
            curr_nl = curr_nl.next
            curr_1 = curr_1.next
        else:
            curr_nl.next = curr_2
            curr_nl = curr_nl.next
            curr_2 = curr_2.next
    
    if not curr_2 and curr_1:
        curr_nl.next = curr_1

    elif not curr_1 and curr_2:
        curr_nl.next = curr_2

    return new_list.next