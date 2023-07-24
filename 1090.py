def solve():
    n, x = map(int, input().split())
    children = sorted(list(map(int, input().split())))
    start = 0
    end = n - 1
    result = 0
    while start <= end:
        if children[start] + children[end] > x:
            end -= 1
            result += 1
        else:
            start += 1
            end -= 1
            result += 1
    return result

if __name__ == '__main__':
    print(solve())