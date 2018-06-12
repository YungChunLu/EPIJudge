from test_framework import generic_test


def is_balanced_binary_tree(tree):
    # TODO - you fill in here.
    def helper(root):
        if root:
            is_balanced_left, h_left = helper(root.left)
            if not is_balanced_left:
                return is_balanced_left, 0
            is_balanced_right, h_right = helper(root.right)
            if not is_balanced_right:
                return is_balanced_right, 0
            is_balanced = abs(h_left - h_right) <= 1
            return is_balanced, max(h_left, h_right) + 1
        else:
            return True, -1
    is_balanced, _ = helper(tree)
    return is_balanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
