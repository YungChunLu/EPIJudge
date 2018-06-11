from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x):
    # TODO - you fill in here.
    if x == 0:
        return "0"
    is_negative, zero_code, ans = False, ord("0"), ""
    if x < 0:
        is_negative = True
        x *= -1
    while x:
        ans = chr(x % 10 + zero_code) + ans
        x = x // 10
    return "-" + ans if is_negative else ans


def string_to_int(s):
    # TODO - you fill in here.
    is_negative, ans, zero_code = False, 0, ord("0")
    if s[0] == "-":
        is_negative = True
        s = s[1:]
    while s:
        ans = ans * 10 + (ord(s[0]) - zero_code)
        s = s[1:]
    return ans * -1 if is_negative else ans


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
