import heapq
def solve():
    n = int(input())
    current = []
    times = []
    for _ in range(n):
        arrival, leaving = map(int, input().split())
        times.append((arrival, leaving))
    times.sort(key= lambda x: x[0])
    leaves = []


    result = 0
    current = 0
    for arrival, leaving in times:
        current += 1
        heapq.heappush(leaves, leaving)
        while leaves[0] < arrival:
            heapq.heappop(leaves)
            current -= 1
        result = max(result, current)
    return result

    
if __name__ == '__main__':
    print(solve())