sentence = '''My very photogenic mother died in a freak accident (picnic, lightning)
when I was three, and, save for a pocket of warmth in the darkest past,
nothing of her subsists within the hollows and dells of memory, over which,
if you can still stand my style (I am writing under observation),
the sun of my infancy had set: surely, you all know those redolent remnants of day suspended,
with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler,
at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
sentence = sentence.split()

set_a = {sentence[i].strip('();:.,').lower() for i in range(len(sentence))}

print(*sorted(set_a))

# The program outputs a set containing the unique words (in lower case) of the 'sentence' string.

# The result is displayed on one line in alphabetical order,
# the elements are separated by a single space character.

# Punctuation marks do not apply to words.

# The code is written using a set generator.