"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import random
import string

def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.
    
    pricess_file 遍历文件中的每一行，同时将每行内容逐次传递给 process_line.
    词频 hist 在此处作为累加器使用。

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
   
    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename)

    if skip_header:
        skip_gutenberg_header(fp)

    for line in fp:
        if line.startswith('*** END OF THIS'):
            break

        process_line(line, hist)

    return hist


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THIS'):
            break


def process_line(line, hist):
    """Adds the words in the line to the histogram.

    Modifies hist.

    line: string
    hist: histogram (map from word to frequency)
    """
    # TODO: rewrite using Counter

    # replace hyphens with spaces before splitting
    # 将分隔前的连字符 '-' 替换为空格 ' '
    line = line.replace('-', ' ')
    strippables = string.punctuation + string.whitespace

    for word in line.split():
        # remove punctuation and convert to lowercase
        word = word.strip(strippables)
        word = word.lower()
        # 此处说的是转换，字符串是不可变的。所以像 strip以及lower方法，都是返回新的字符串。

        # update the histogram
        # 
        hist[word] = hist.get(word, 0) + 1


def most_common(hist):
    """Makes a list of word-freq pairs in descending order of frequency.

    hist: map from word to frequency

    returns: list of (frequency, word) pairs
    """
    t = []
    for key, value in hist.items():
        t.append((value, key))

    # 将词频词典遍历，取出次数当值，key变成value，变成新字典列表。
    # 所有结果入列表后，先排一次序，然后再反转，将列表倒序。
    t.sort()
    t.reverse()
    return t


def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.
    
    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[:num]:
        print(word, '\t', freq)


def subtract(d1, d2):
    """Returns a dictionary with all keys that appear in d1 but not d2.
    返回一个字典，其中包含 d1 中出现但 d2 中不出现但所有键。

    d1, d2: dictionaries
    """
    # TODO: reimplement using Counter
    res = {}
    # 遍历字典1，取出每个值，然后判断是否存在d2里，如果不存在的写入字典。
    for key in d1:
        if key not in d2:
            res[key] = None
    return res


def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    # 通过sum来获得hist的值，我怎么想不到。sum里面也是一个迭代器，我传入字典的value集合就取出来值。
    return sum(hist.values())


def different_words(hist):
    """Returns the number of different words in a histogram."""
    # 而这里更是简单，直接计算字典的大小就得到了不同单词的数量，不用管values。
    # 都是对基础操作的灵活应用，而我因为没有熟练掌握，所以对这样的功能实现束手无策。
    # 正是这样每一步都差一点儿，所以才做不成好的工程师，所以开发效率极慢。
    # 这和使用什么语言编码都毫无关系，我的Java编程能力也不行，现在来看Python更轻便快捷。
    return len(hist)


def random_word(hist):
    """Chooses a random word from a histogram.

    The probability of each word is proportional to its frequency.
    """
    # TODO: rewrite using Counter
    t = []
    # 这里是将所有单词都放入集合列表里，一个单词出现多少次就复制多少遍，
    # 然后用random.choice()从里面随机取一个，就实现了按词频正比返回随机数了。
    for word, freq in hist.items():
        t.extend([word] * freq)
    
    # [word] * freq: 会生成一个包含word 的列表，并且长度为 freq。
    # t.extend([...])：会将方括号里面的所有元素逐个添加到列表t中。
    # 例如：t.extend(['hello', 'hello', 'hello']) 会将 'hello' 三次添加到列表 t 中。

    return random.choice(t)


def main():
    hist = process_file('/Users/dengwentao/work/python_project/ThinkPython2-CN/code/158-0.txt', skip_header=True)
    print('Total number of words:', total_words(hist))
    print('Number of different words:', different_words(hist))

    t = most_common(hist)
    print('The most common words are:')
    # 使用切片取出前20个。t[0:20]
    for freq, word in t[0:20]:
        print(word, '\t', freq)

    words = process_file('/Users/dengwentao/work/python_project/ThinkPython2-CN/code/words.txt', skip_header=False)

    # 这里取出出现在单词书中，但不在单词表汇总的词汇。
    diff = subtract(hist, words)
    print("The words in the book that aren't in the word list are:")
    for word in diff.keys():
        print(word, end=' ')

    print("\n\nHere are some random words from the book")
    for i in range(100):
        print(random_word(hist), end=' ')


if __name__ == '__main__':
    main()


