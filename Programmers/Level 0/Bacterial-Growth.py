def solution(n, t):
    for i in range(t):
        n *= 2

    return n

def solution2(n, t):
    return 2 ** t * n  # e.g n:2 = 2^10 * n = 2048

def solution3(n, t):
    return n << t

# --------- input ------------
n, t = 2, 10
print(solution(n, t))