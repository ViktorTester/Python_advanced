dict1 = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}

s = list(input())
arr = []

for i in range(len(s)):
    for key, value in dict1.items():
        if key in s[i]:
            arr.append(value)

arr = "".join(arr)

print(arr)

# As is known from the course of biology, DNA and RNA are nucleotide sequences.

# Four nucleotides in DNA:

# adenine (A);
# cytosine (C);
# guanine (G);
# thymine (T).
# Four nucleotides in RNA:

# adenine (A);
# cytosine (C);
# guanine (G);
# uracil (U).

# The RNA chain is built on the basis of the DNA chain by
# the sequential addition of complementary nucleotides:

# G→C;
# C→G;
# T→A;
# A→U.

# The program converts a DNA strand into an RNA strand.