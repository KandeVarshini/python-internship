def min_ascii_distance(A, S):
    if set(S).issubset(set(A)):
        return 0

    total_distance = 0

    for char_a in A:
        min_distance = float('inf')
        for char_s in S:
            distance = abs(ord(char_a) - ord(char_s))
            if distance < min_distance:
                min_distance = distance

        total_distance += min_distance

    return total_distance

if __name__ == "__main__":
    A = input().strip()
    S = input().strip()
    print(min_ascii_distance(A, S))
