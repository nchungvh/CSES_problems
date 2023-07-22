def solve():
    n = int(input())
    numbers = map(int, input().split())
    check = [False] * n
    for number in numbers:
        check[number - 1] = True
    for i in range(n):
        if check[i] == False:
            return i + 1


if __name__ == '__main__':
    print(solve())