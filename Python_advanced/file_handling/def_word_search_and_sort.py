"""The input is a file containing many non-unique words. The program finds in it all
the words ending with the string 'EY', and displays them on the screen. Wherein:

eliminates duplicates
converts all letters to uppercase
arranges the words in the output in double sort order:
first sorts in ascending order of word length,
and alphabetizes if the lengths are the same"""


def word_search_and_sort(file_name: str):
    with open(file_name, encoding='utf-8') as file:
        my_set = {j.upper() for j in file.read().split() if j.endswith('ey')}

        for i in sorted(my_set, key=lambda x: ((len(x)), x)):
            print(i)


word_search_and_sort(input())
