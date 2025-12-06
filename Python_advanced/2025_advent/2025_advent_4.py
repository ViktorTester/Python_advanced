def countAccessibleRolls(plan):
    rows = len(plan)
    cols = len(plan[0])

    neighbors = [(-1, -1), (-1, 0), (-1, 1),
                 (0, -1), (0, 1),
                 (1, -1), (1, 0), (1, 1)]

    accessible = 0

    for r in range(rows):
        for c in range(cols):
            if plan[r][c] != '@':
                continue

            count = 0
            for dr, dc in neighbors:
                new_row = r + dr
                new_column = c + dc
                if 0 <= new_row < rows and 0 <= new_column < cols:
                    if plan[new_row][new_column] == '@':
                        count += 1

            if count < 4:
                accessible += 1

    return accessible


with open("test.txt", "r", encoding="utf-8") as f:
    lines = [line.rstrip("\n") for line in f]

print(countAccessibleRolls(lines))
