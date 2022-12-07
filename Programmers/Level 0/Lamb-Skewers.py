def solution(n, k):
    service = n // 10
    result = 12000 * n + (2000 * (k - service))
    return result

# --------- input ------------
n, k = 10, 3
print(solution(n, k))