"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

"""

WARNING: this program contains a NASTY bug.  I put
it there on purpose as a debugging exercise, but
you DO NOT want to emulate this example!

"""

class Kangaroo:
    """A Kangaroo is a marsupial."""
    
    # 在Python中，如果一个函数或方法的参数使用了一个可变对象（例如列表、字典等）作为默认值，
    # 那么所有使用该默认值的对象都会共享一个对象。
    def __init__(self, name, contents=None):
        """Initialize the pouch contents.

        name: string
        contents: initial pouch contents.
        """
        self.name = name
        if contents is None:
            contents = []
        self.pouch_contents = contents

    def __str__(self):
        """Return a string representaion of this Kangaroo.
        """
        t = [ self.name + ' has pouch contents:' ]
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, item):
        """Adds a new item to the pouch contents.

        item: object to be added
        """
        self.pouch_contents.append(item)


kanga = Kangaroo('Kanga')
roo = Kangaroo('Roo')
# kanga.put_in_pouch('wallet')
# kanga.put_in_pouch('car keys')
kanga.put_in_pouch(roo)

print(kanga)

# If you run this program as is, it seems to work.
# To see the problem, trying printing roo.

# Hint: to find the problem try running pylint.
