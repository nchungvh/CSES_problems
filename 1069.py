def solve():
    String = input()
    length = len(String)
    result = 1
    current_length = 1
    for index in range(1, length):
        if String[index] != String[index - 1]:
            result = max(result, current_length)
            current_length = 1
        else:
            current_length += 1
    return max(result, current_length)

if __name__ == '__main__':
    print(solve())