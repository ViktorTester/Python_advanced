"""The get_word_indices function takes a list of strings and returns
a dictionary, where keys are unique lowercase words from a list of
strings, and values are lists of string indices in which those words occur."""


def get_word_indices(strings: list[str]) -> dict:
    word_indices = {}
    for i, string in enumerate(strings):
        words = string.lower().split()
        for word in words:
            if word not in word_indices:
                word_indices[word] = [i]
            else:
                word_indices[word].append(i)
    return word_indices
