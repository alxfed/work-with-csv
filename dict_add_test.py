"""
Rumors say that dictionaries have become ordered in 3.7. Let's see...
"""
from collections import OrderedDict

di = {}
a = {'a': 246}
b = {'b': 247}
c = {'de': 1}

di.update(a)
di.update(b)
di.update(c)

odi = OrderedDict()

odi.



print(di.popitem())
print(di.popitem())
print(di.popitem())
