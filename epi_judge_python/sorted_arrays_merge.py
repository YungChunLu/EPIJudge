from test_framework import generic_test
import heapq

def merge_sorted_arrays(sorted_arrays):
    # TODO - you fill in here.
    min_heap, array_len, ans = [], [], []
    for k, array in enumerate(sorted_arrays):
        L = len(array)
        array_len.append(L)
        if L:
            heapq.heappush(min_heap, (array[0], k, 0))
    while min_heap:
        val, k, idx = heapq.heappop(min_heap)
        ans.append(val)
        idx += 1
        if idx < array_len[k]:
            heapq.heappush(min_heap, (sorted_arrays[k][idx], k, idx))
    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
