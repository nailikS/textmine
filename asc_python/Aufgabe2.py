import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import time

x = [s + 1 for s in range(1000000)]
y = [a + 1 for a in range(10)]
d = dict(zip(x, x))
d2 = dict(zip(y, y))
performance = []

# just for testing purpose, the 2 is missing i know.
# 1. Test: plain list comprehension
t1 = time.perf_counter()
prime1 = [e for e in x if e % 2 != 0]
t11 = time.perf_counter()
performance.append(t11-t1)
# 2. Test: plain list for loop
t2 = time.perf_counter()
erg1 = []
for e in x:
    if e % 2 != 0:
        erg1.append(e)
t22 = time.perf_counter()
performance.append(t22-t2)
# 3. Test: plain dict comprehension
t3 = time.perf_counter()
newd = {e: e for e in d.values() if e % 2 != 0}
t33 = time.perf_counter()
performance.append(t33-t3)
# 4. Test: plain dict for loop
t4 = time.perf_counter()
erg4 = {}
for e in x:
    if e % 2 != 0:
        erg4[e] = e
t44 = time.perf_counter()
performance.append(t44-t4)
# 5. Test: With if-else list comprehension
t5 = time.perf_counter()
prime5 = [e if e % 2 != 0 else 0 for e in x]
t55 = time.perf_counter()
performance.append(t55-t5)
# 6. Test: With if-else list for-loop
t6 = time.perf_counter()
erg6 = []
for e in x:
    if e % 2 != 0:
        erg6.append(e)
    else:
        erg6.append(0)
t66 = time.perf_counter()
performance.append(t66-t6)
# 7. Test: With if-else dictionary comprehension
t7 = time.perf_counter()
newd7 = {e: e if e % 2 != 0 else 0 for e in d.values()}
t77 = time.perf_counter()
performance.append(t77-t7)
# 8. Test: With if-else dictionary for-loop
t8 = time.perf_counter()
erg8 = {}
for e in d.values():
    if e % 2 != 0:
        erg8[e] = e
    else:
        erg8[e] = 0
t88 = time.perf_counter()
performance.append(t88-t8)
# 9. Test: two list comprehension
t9 = time.perf_counter()
product = [i * j for i in x for j in y]
t99 = time.perf_counter()
performance.append(t99-t9)
# 10. Test: two list for-loop
t10 = time.perf_counter()
erg10 = []
for e in x:
    for m in y:
        erg10.append(e * m)
t1010 = time.perf_counter()
performance.append(t1010-t10)
# 11. Test: two dictionary comprehension
t111 = time.perf_counter()
newd11 = {(e, m): e * m for e in d.values() for m in d2.values()}
t1111 = time.perf_counter()
performance.append(t1111-t111)
# 12. Test: two dictionary for-loop
t12 = time.perf_counter()
erg12 = {}
for e in d.values():
    for m in d2.values():
        erg12[(e, m)] = e * m
t1212 = time.perf_counter()
performance.append(t1212-t12)

objects = ('plain list comprehension', 'plain list for loop', 'plain dict comprehension',
           'plain dict for loop', 'With if-else list comprehension', 'With if-else list for-loop',
           'With if-else dictionary comprehension', 'With if-else dictionary for-loop', 'two list comprehension',
           'two list for-loop', 'two dictionary comprehension', 'two dictionary for-loop')
y_pos = np.arange(len(objects))
plt.barh(y_pos, performance, align='center', alpha=0.5)
plt.yticks(y_pos, objects)
plt.xlabel('time in s')
plt.title('Performance Benchmark')
plt.show()
