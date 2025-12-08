with open("test.txt", "r", encoding="utf-8") as f:
    rows = [list(line.rstrip()) for line in f if line.strip()]

start_col = rows[0].index("S")

rows_n = len(rows)
cols_n = len(rows[0])

beams = {start_col}
activated = set()

for r in range(1, rows_n):
    next_beams = set()

    for col in beams:
        if not (0 <= col < cols_n):
            continue

        cell = rows[r][col]

        if cell == ".":
            next_beams.add(col)

        elif cell == "^":
            activated.add((r, col))

            if col - 1 >= 0:
                next_beams.add(col - 1)
            if col + 1 < cols_n:
                next_beams.add(col + 1)

    beams = next_beams

print(len(activated))
