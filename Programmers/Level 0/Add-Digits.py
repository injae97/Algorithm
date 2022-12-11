def solution(n):
    result = 0
    n = list(map(int, str(n))) # 1234 -> [1, 2, 3, 4]
    for i in range(len(n)):
        result += n[i]

    return result

# --------- input ------------
n = 1234
print(solution(n))