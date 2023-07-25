def solve():
    n = int(input())
    array = list(map(int, input().split()))
    length = len(array)
    def calculate(value):
        return sum([abs(num - value) for num in array])
    start = min(array)
    end = max(array)
    while start < end:
        mid = (start + end) // 2
        mid_sum = calculate(mid)
        right_sum = calculate(mid + 1)
        if mid_sum < right_sum:
            end = mid
        elif mid_sum > right_sum:
            start = mid + 1
        else:
            return mid_sum
    return calculate(end)

if __name__ == '__main__':
    print(solve())