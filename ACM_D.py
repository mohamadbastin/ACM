#D


def spliter(x):
    a = x.split('1')
    return a


def ans(x):
    return len(max(spliter(x)))


x = input()
print(ans(x))
