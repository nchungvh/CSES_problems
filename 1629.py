def solve():
    n = int(input())
    current = []
    times = []
    for _ in range(n):
        start, end = map(int, input().split())
        times.append((start, end))
    times.sort(key= lambda x: x[1])

    result = 1
    last_end = times[0][1]
    for start, end in times:
        if start >= last_end:
            last_end = end
            result += 1
    return result

    
if __name__ == '__main__':
    print(solve())