def solve():
    n, x = map(int, input().split())
    array = map(int, input().split())

    array = sorted([(i, num) for i, num in enumerate(array)], key= lambda x: x[1])
    start = 0
    end = len(array) - 1

    while start < end:
        if array[start][1] + array[end][1] > x:
            end -= 1
        elif array[start][1] + array[end][1] < x:
            start += 1
        else:
            return f'{array[start][0] + 1} {array[end][0] + 1}'
    return 'IMPOSSIBLE'


if __name__ == '__main__':
    print(solve())