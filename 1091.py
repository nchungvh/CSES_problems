def solve():
    # must use balanced binary tree to delete element with O(log(n)) to resolve TLE tests
    n, m = map(int, input().split())
    tickets = sorted(list(map(int, input().split())))
    customers = map(int, input().split())
    checks = [True] * n
    result = []
    for customer in customers:
        start = 0
        end = n - 1
        while start < end:
            mid = (start + end) // 2
            if tickets[mid] < customer:
                start = mid + 1
            elif tickets[mid] > customer:
                end = mid - 1
            else:
                while tickets[mid] == customer and mid < end:
                    mid += 1
                end = mid
                break
        while end >= 0:
            if tickets[end] <= customer and checks[end]:
                checks[end] = False
                result.append(str(tickets[end]))
                break
            end -= 1
        if end == -1:
            result.append('-1')
    return '\n'.join(result)

if __name__ == '__main__':
    print(solve())