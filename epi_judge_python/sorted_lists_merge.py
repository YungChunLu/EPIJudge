from test_framework import generic_test
from list_node import ListNode


def merge_two_sorted_lists(L1, L2):
    # TODO - you fill in here.
    merged_list = ListNode()
    dummy_head = merged_list
    while L1 and L2:
        if L1.data < L2.data:
            dummy_head.next = ListNode(data=L1.data)
            L1 = L1.next
        else:
            dummy_head.next = ListNode(data=L2.data)
            L2 = L2.next
        dummy_head = dummy_head.next
    if L1:
        dummy_head.next = L1
    elif L2:
        dummy_head.next = L2
    return merged_list.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_lists_merge.py",
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
