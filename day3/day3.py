import re

int_conv = lambda x : [int(i) for i in x]

reg = r"mul\(\d{1,3},\d{1,3}\)"
cont = ''.join([line.strip() for line in open("day3input.txt")])

matches = re.findall(reg, cont)

t = 0

for match in matches:
    m1, m2 = int_conv(re.findall(r"\d{1,3}", match))
    t += (m1 * m2)

reger = r"don't\(\)|do\(\)|mul\(\d{1,3},\d{1,3}\)"
matches = re.findall(reger, cont)

s = 0
is_on = True

for match in matches:
    print(match, is_on)
    if match == "don't()":
        print("off")
        is_on = False
        continue
    if match == "do()":
        print("on")
        is_on = True
        continue

    if is_on:
        m1, m2 = int_conv(re.findall(r"\d{1,3}", match))
        s += (m1 * m2)


print(s)
