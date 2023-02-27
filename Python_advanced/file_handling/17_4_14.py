with open('logfile.txt', encoding='utf-8') as file1, open(
        'output.txt', 'w', encoding='utf-8') as file2:
    for line in file1:
        name, surname, s_time, e_time = line.split()
        s_time = int(s_time[:2]) * 60 + int(s_time[3:5])
        e_time = int(e_time[:2]) * 60 + int(e_time[3:5])
        surname = surname[:-1]
        if e_time - s_time > 59:
            print(name, surname, file=file2)

# There is a text file logfile.txt with information about the time the user logged in
# and out of the system. Each line of the file contains three values separated by commas
# and a space character: username, login time, logout time, where the time is in 24-hour format.

# The program creates an output.txt file and displays the names of all users
# (without changing the order) who have been online for at least an hour.
