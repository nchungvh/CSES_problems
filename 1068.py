def solve():
    n = int(input())
    result = [str(n)]
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        result.append(str(n))
    return ' '.join(result)

if __name__ == '__main__':
    print(solve())