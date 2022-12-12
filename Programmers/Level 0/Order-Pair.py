def solution(n):
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0:
            # print(f"({i}, {n//i})")      output : (1, 20), (2, 10), (4, 5), (5, 4), (10, 2), (20, 1)
            cnt += 1

    return cnt

def solution2(n):
    answer = []
    for i in range(1, n+1):
        if n % i == 0:
            answer.extend([(i, n//i)])

    return len(answer)

# --------- input ------------
n = 20
print(solution(n))