def solve():
    n, m, k = map(int, input().split())
    desired = sorted(list(map(int, input().split())))
    apartments = sorted(map(int, input().split()))
    desired_length = len(desired)
    apartments_length = len(apartments)

    desired_index = 0
    apartments_index = 0
    result = 0
    while desired_index < desired_length and apartments_index < apartments_length:
        if apartments[apartments_index] - k <= desired[desired_index] <= apartments[apartments_index] + k:
            desired_index += 1
            apartments_index += 1
            result += 1
        elif desired[desired_index] < apartments[apartments_index] - k:
            desired_index += 1
        else:
            apartments_index += 1
    return result

if __name__ == '__main__':
    print(solve())