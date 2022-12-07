def solution(n):
    result = 0
    for i in range(0, n + 1):
        if i % 2 == 0:
            result += i

    return result

def solution2(n):
    return sum([i for i in range(2, n + 1, 2)])

# --------- input ------------
n = 10
print(solution(n))