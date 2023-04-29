formats = {'write read execute'.split()[i]: 'WRX'[i] for i in range(3)}
accesses = {}

for _ in range(int(input())):
    s = input().split()
    file, *options = s
    accesses[file] = options

for _ in range(int(input())):
    frmt, file = input().split()
    print('OK' if formats[frmt] in accesses[file] else 'Access denied')

# A dangerous virus has penetrated the computer's file system and broken file access control.

# For each file, it is known what actions can be accessed with it:

# write W (write, access to write to a file);
# reading R (read, access to read from a file);
# launch X (execute, launch for file execution).

# The program restores file access control. For each request, the program returns 'OK'
# if a valid operation is performed, and 'Access denied' if the operation is invalid.

# The program receives as input the number of files 'n' contained in the file system
# of the computer. Then there are n lines, each containing the name of the file and the
# operations allowed with it, separated by a space character.
# The next line contains the number 'm' — the number of file requests,
# and then m lines with requests of the file operation type.
# Any number of requests can be addressed to the same file.