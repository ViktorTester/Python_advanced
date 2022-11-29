s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'

s = s.replace(':', ' ').split()

for i in range(len(s)):
    if i % 2 == 0:
        s[i] = int(s[i])

arr1, arr2 = [], []

for x in range(len(s)):
    if x % 2 == 0:
        arr1.append(s[x])
    else:
        arr2.append(s[x])

result = dict(zip(arr1, arr2))

print(result)

# Can be replaced with the following code:

result = {int(k):v for k, v in [l.split(':') for l in s.split()]}

# Can be replaced with the following code:

result = {}

for i in s.split():
    key, value = i.split(':')
    result[int(key)] = str(value)

# The variable 's' stores a string of number:word pairs. The program, using a generator,
# outputs a dictionary 'result', in which numbers will be keys and words will be values.