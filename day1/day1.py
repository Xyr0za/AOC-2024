from collections import Counter

cont = [line.strip().split(' ') for line in open("day1input.txt").readlines()]

l1 = sorted([int(i[0]) for i in cont])
l2 = sorted([int(i[-1]) for i in cont])

t = 0 

l2hash = dict(Counter(l2))

for i, j in zip(l1,l2):
    t += abs(i-j)


print(t)

s = 0

for i in l1:
    if not i in l2hash.keys():
        continue
    s += l2hash.get(i) * i

print(s)
