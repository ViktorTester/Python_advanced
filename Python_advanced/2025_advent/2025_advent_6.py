with open("/Users/aggro/PycharmProjects/Python_advanced/Python_advanced/bool_and_NoneType/test.txt", "r",
          encoding="utf-8") as f:
    data = f.read()

values = data.split()
numbers, signs, arr = [], [], []
grand_result = 0

for i in values:
    if i != "+" and i != "*":
        arr.append(int(i))
        if len(arr) == 3:
            numbers.append(arr)
            arr = []
    else:
        signs.append(i)

print(numbers)

for j, x in enumerate(numbers):
    if signs[j] == "+":
        column_result = 0
        for y in x:
            column_result += y
    else:
        column_result = 1
        for y in x:
            column_result *= y
    grand_result += column_result

print(grand_result)
