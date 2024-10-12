"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division


def signature(s):
    """Returns the signature of this string.

    Signature is a string that contains all of the letters in order.

    s: string
    """
    # TODO: rewrite using sorted()
    t = list(s)
    t.sort()
    t = ''.join(t)
    # 将单词转成字符串列表，进行排序后再拼接成字母字符串。
    return t


def all_anagrams(filename):
    """Finds all anagrams in a list of words.

    filename: string filename of the word list

    Returns: a map from each word to a list of its anagrams.
    """
    # anagrams 颠倒字母而成的字
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)

        # TODO: rewrite using defaultdict
        # 将所有变位词组成的单词都放到集合里存储起来。例如。enp是单词排序后的字母字符串，对应的单词里有['pen']
        
        # 有些知识，你不知道就是不知道。你能说这些技术没用吗？在你真的学它之前，它好像真的没用，因为你没用它照样活的好好的。
        # 可当你学会这些之后，就变得不一样的，你的技术更上一层楼，填补了更细的知识，你的知识面更广了。
        # 它不是用来应付面试的八股文，而是真的能切实提升你编程能力和速度的技能。
        if t not in d:
            # 如果这个变位词不存在字典中，就以它作key，将word放入集合中。
            d[t] = [word]
        else:
            # 如果存在，就将新单词放入集合中，最终返回字典。
            d[t].append(word)
    return d


def print_anagram_sets(d):
    """Prints the anagram sets in d.

    d: map from words to list of their anagrams
    """
    for v in d.values():
        if len(v) > 1:
            print(len(v), v)


def print_anagram_sets_in_order(d):
    """Prints the anagram sets in d in decreasing order of size.
    按从大到小递减的顺序打印 d 中的字符集

    d: map from words to list of their anagrams
    d: 将单词映射到它们的字符列表。
    """
    # make a list of (length, word pairs)
    t = []
    for v in d.values():
        # 遍历每个元素，将字符按照长度作key来存放，value是字符
        if len(v) > 1:
            t.append((len(v), v))

    # sort in ascending order of length
    # 这里将列表升序排序，然后打印输出
    t.sort()

    # print the sorted list
    for x in t:
        print(x)


def filter_length(d, n):
    """Select only the words in d that have n letters.

    d: map from word to list of anagrams
    n: integer number of letters

    returns: new map from word to list of anagrams
    """
    res = {}
    # 这里是将字典遍历，取出变位词和对应的单词列表。如果长度等于8，将单词列表写入。
    for word, anagrams in d.items():
        if len(word) == n:
            res[word] = anagrams
    return res


if __name__ == '__main__':
    anagram_map = all_anagrams('/Users/dengwentao/work/python_project/ThinkPython2-CN/code/words.txt')
    print_anagram_sets_in_order(anagram_map)

    eight_letters = filter_length(anagram_map, 8)
    print_anagram_sets_in_order(eight_letters)
    
