def solve():
    n = int(input())
    array = map(int, input().split())
    check = set()
    for i in array:
        if i - 1 in check:
            check.remove(i - 1)
        check.add(i)
    return len(list(check))

if __name__ == '__main__':
    print(solve())