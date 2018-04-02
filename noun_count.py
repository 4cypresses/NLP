>>> import sys
>>> orig_stdout = sys.stdout
>>> f = open('out.txt', 'w')
>>> sys.stdout = f
>>> f1 = open('output1.txt')
>>> data = f1.read()
>>> words = {}
>>> for word in data.split():
...     words[word] = words.get(word, 0) + 1
...
>>> d = [(v,k) for k,v in words.items()]
>>>
>>> d.sort()
>>> d.reverse()
>>> for count, word in d:
...     print(count, word)
...
>>> sys.stdout = orig_stdout
>>> f.close()