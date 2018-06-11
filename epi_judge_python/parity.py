from test_framework import generic_test


def parity(x):
    # TODO - you fill in here.
    ans = 0
    while x:
        ans = (x&1)^ans
        x = x >> 1
    return ans


if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
