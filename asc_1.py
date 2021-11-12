import sys
import matplotlib.pyplot as plt
import numpy as np

rawData = dict()
working_on = ""
basestring = ""
alphabet = ['A', 'C', 'G', 'T']
baseData = dict()
totals = []

fasta = open(str(sys.argv[1]), 'r')
for line in fasta:
    if line[0] == ">":
        rawData[line[0:10]] = ""
        working_on = line[0:10]
        basestring = ""
    else:
        basestring += line.strip()
        rawData[working_on] = basestring

for key in list(rawData.keys()):
    baseStats = dict()
    k = 0
    for letter in alphabet:
        n = rawData[key].count(letter)
        baseStats[letter] = n
        k += n
    totals.append(k)
    baseData[key] = baseStats
totals.append(sum(totals))


def reorder(char):
    nums = []
    for key in list(rawData.keys()):
        nums.append(baseData[key][char])
    return nums


def percentages(char):
    nums = []
    if char == 'Total':
        for l in alphabet:
            num = []
            for key in list(rawData.keys()):
                num.append(baseData[key][l])
            nums.append(sum(num))
        return [round(n / totals[3] * 100, 1) for n in nums]
    else:
        for i in range(len(list(rawData.keys()))):
            keys = list(rawData.keys())
            nums.append(round(baseData[keys[i]][char] / totals[i] * 100, 1))
        return nums


A = reorder('A')
C = reorder('C')
G = reorder('G')
T = reorder('T')
labels = list(baseData.keys())
x = np.arange(len(labels))  # the label locations
width = 0.8  # the width of the bars

tot = percentages('Total')
a = percentages('A')
a.append(tot[0])
c = percentages('C')
c.append(tot[1])
g = percentages('G')
g.append(tot[2])
t = percentages('T')
t.append(tot[3])

labels2 = labels.copy()
labels2.append('Total')
x2 = np.arange(len(labels2))
w = 0.5

fig, (ax1, ax2) = plt.subplots(2)
rects1 = ax1.bar(x - (width/4*1.5), A, width/4, label='A')
rects2 = ax1.bar(x - (width/4*0.5), C, width/4, label='C')
rects3 = ax1.bar(x + (width/4*0.5), G, width/4, label='G')
rects4 = ax1.bar(x + (width/4*1.5), T, width/4, label='T')

ax1.set_ylabel('n')
ax1.set_title('Total Number of Bases')
ax1.set_xticks(x)
ax1.set_xticklabels(labels)
ax1.legend()

ax1.bar_label(rects1, padding=3)
ax1.bar_label(rects2, padding=3)
ax1.bar_label(rects3, padding=3)
ax1.bar_label(rects4, padding=3)

rects11 = ax2.bar(x2 - (width/4*1.5), a, width/4, label='A')
rects22 = ax2.bar(x2 - (width/4*0.5), c, width/4, label='C')
rects33 = ax2.bar(x2 + (width/4*0.5), g, width/4, label='G')
rects44 = ax2.bar(x2 + (width/4*1.5), t, width/4, label='T')

ax2.set_ylabel('n')
ax2.set_title('Percentages of each base')
ax2.set_xticks(x2)
ax2.set_xticklabels(labels2)
ax2.legend()

ax2.bar_label(rects11, padding=3)
ax2.bar_label(rects22, padding=3)
ax2.bar_label(rects33, padding=3)
ax2.bar_label(rects44, padding=3)

fig.tight_layout()
plt.show()
