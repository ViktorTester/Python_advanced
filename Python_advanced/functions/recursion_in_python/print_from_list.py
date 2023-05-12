N = int(input())
s = list(map(int, input().split()))


def print_list(N: int):
    if N > 0:
        print_list(N - 1)
        print(s[-N], end=' ')

print_list(N)

#The program receives a natural number N and a sequence of N elements as input.
# The program outputs this sequence in reverse order.