def DP(arr, value):
    pass

def solve():
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    result = 1
    for num in arr:
        if num > result:
            break
        result += num
    return result

if __name__ == '__main__':
    print(solve())