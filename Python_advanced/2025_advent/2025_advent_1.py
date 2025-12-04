import re

arr, s, p, counter = [], 50, 0, 0

with open("test.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()

        if re.fullmatch(r"[LR]\d+", line):
            arr.append(line)

for i in arr:
    if len(i) >= 4:
        p = str(int(i[1::]) % 100)
        i = i[0] + p

    if i[0] == "L":
        s = (s - int(i[1::]))
        if s <= 0:
            s = s + 100
    else:
        s = (s + int(i[1::]))
        if s > 100:
            s = s - 100

    if s == 100:
        counter += 1

print(counter)
