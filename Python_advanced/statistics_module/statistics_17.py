from statistics import multimode as mm

with open('students.csv', encoding='utf-8') as file:
    text = [line.strip().split(',') for line in file.readlines()]
    arr = [text[i][1] for i in range(1, len(text))]
    most_popular = mm(arr)

    print(*most_popular)

# There is a students.csv file containing student data. The first column contains
# the last name, the second - the first name, and the third - progress on the
# course as a percentage. The program determines the most popular name and
# displays it with a capital letter. If there are several such names,
# the program displays them separated by
# commas in alphabetical order, each with a capital letter.