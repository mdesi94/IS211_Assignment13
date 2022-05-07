# Part 1
def fibonnaci(n):
    if n <= 1:
        return n
    else:
        return fibonnaci(n - 1) + fibonnaci(n - 2)


# Part 2
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


# Part 3
def compareTo(s1, s2):
    if len(s1) == 0 and len(s2) == 0:
        return 0
    elif len(s1) == 0:
        return -1
    elif len(s2) == 0:
        return 1

    if s1[0] < s2[0]:
        return -1
    elif s1[0] > s2[0]:
        return 1
    else:
        return compareTo(s1[1:], s2[1:])


# test functions
if __name__ == '__main__':
    print(fibonnaci(15))
    print(gcd(90, 120))
    print(compareTo('king', 'mouse'))