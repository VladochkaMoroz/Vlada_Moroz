from itertools import permutations


def nextBigger(num):
    k = sorted(list(map(int, (list(map(lambda x: ''.join(x), set(list(permutations(str(num), len(str(num)))))))))))
    i = k.index(num)
    return -1 if i >= len(k) - 1 else k[i + 1]


print(nextBigger(12))
