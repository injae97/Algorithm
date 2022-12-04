def solution(n):
    result = 0
    for i in range(0, n+1):
        if i % 2 == 0:
            result += i

    return result

# --------- input ------------
n = 10
print(solution(n))