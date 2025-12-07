ranges = []
ids = []

with open("test.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        if '-' in line:
            ranges.append(line)
        else:
            ids.append(line)

counter = 0

for i in ids:
    for j in ranges:
        s = j.split("-")
        left, right = int(s[0]), int(s[1])
        if left <= int(i) <= right:
            counter += 1
            break

print(counter)
