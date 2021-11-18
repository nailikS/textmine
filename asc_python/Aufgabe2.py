import random
import time

x = [s+1 for s in range(100000)]
y = [a+1 for a in range(10)]
d = dict(zip(x, x))
d2 = dict(zip(y, y))
print(d)
print(y)
# just for testing purpose, the 2 is missing i know.
# 1. Test: plain list comprehension
prime1 = [e for e in x if e % 2 != 0]
# 2. Test: plain list for loop
erg1 = []
for e in x:
    if e % 2 != 0:
        erg1.append(e)
# 3. Test: plain dict comprehension
newd = {e: e for e in d.values() if e % 2 != 0}
# 4. Test: plain dict for loop
erg4 = {}
for e in x:
    if e % 2 != 0:
        erg4[e] = e
# 5. Test: With if-else list comprehension
prime5 = [e if e % 2 != 0 else 0 for e in x]
# 6. Test: With if-else list for-loop
erg6 = []
for e in x:
    if e % 2 != 0:
        erg6.append(e)
    else:
        erg6.append(0)
# 7. Test: With if-else dictionary comprehension
newd7 = {e: e if e % 2 != 0 else 0 for e in d.values()}
# 8. Test: With if-else dictionary for-loop
erg8 = {}
for e in d.values():
    if e % 2 != 0:
        erg8[e] = e
    else:
        erg8[e] = 0
# 9. Test: two list comprehension
product = [x * y for x in x for y in y]
# 10. Test: two list for-loop
erg10 = []
for e in x:
    for m in y:
        erg10.append(e * m)
# 11. Test: two dictionary comprehension
newd11 = {(e, m): e * m for e in d.values() for m in d2.values()}
# 12. Test: two dictionary for-loop
erg12 = {}
for e in d.values():
    for m in d2.values():
        erg12[(e, m)] = e * m

