files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp',
         'pen.txt', 'phone.py', 'book.txT', 'board.pNg', 'keyBoard.jpg',
         'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop',
         'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git']

set_a = {files[i].lower() for i in range(len(files)) if files[i][-4:].lower() == '.png'}

print(*sorted(set_a))

# The program selects from the 'files' list unique filenames
# with the .png extension, regardless of the case of names and extensions.

# The filenames are displayed along with the extension,
# all on one line, in lower case, in alphabetical order, separated by a space.

# The code is written using a set generator.
