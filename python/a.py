#!/usr/bin/env python
li = [1,3,5,5,6,1,1,3,1,12,3,2,13,2]
#method 1
result = None
try:
    result = list(set(li))
except TypeError:
    pass

#method 2
t = list(li)
try:
    t = s.sort()
except TypeError:
    del t
else:
    result = [x for i,x in enumerate(t) if not i or x != t[i-1] ]

u = []
for x in li:
    if x not in u:
        u.append(x)
return u



