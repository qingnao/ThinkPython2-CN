"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division


def has_duplicates(t):
    """Checks whether any element appears more than once in a sequence.

    Simple version using a for loop.

    t: sequence
    """
    # d = {}
    # for x in t:
    #     if x in d:
    #         return True
    #     d[x] = True
    # return False

    d = {}
    # 进行循环遍历，判断元素是否存在字典中，如果存在就返回true，否则放入字典。循环结束时返回false。
    for x in t:
        if x in d:
            return True
        d[x] = True
    return False


def has_duplicates2(t):
    """Checks whether any element appears more than once in a sequence.

    Faster version using a set.

    t: sequence
    """
    # 这个就简单多了，直接判断长度，如果是set集合，有重复的长度会减少。高下立判，不用循环遍历。
    return len(set(t)) < len(t)


if __name__ == '__main__':
    t = [1, 2, 3]
    print(has_duplicates(t))
    t.append(1)
    print(has_duplicates(t))

    t = [1, 2, 3]
    print(has_duplicates2(t))
    t.append(1)
    print(has_duplicates2(t))

