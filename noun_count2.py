f = open('out.txt')
text = f.read()
f.close()

import MeCab
import sys
import re
from collections import Counter
m = MeCab.Tagger()
node = m.parseToNode(text)
words=[]
while node:
...     words.append(node.surface)
...     node = node.next
c = collections.Counter(words)
print(c.most_common(30))
