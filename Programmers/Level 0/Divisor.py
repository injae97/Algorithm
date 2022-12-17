def solution(n):
    answer = []
    for i in range(1, n+1):
        if n % i == 0:
            answer.append(i)

    return answer

def solution2(n):
    answer = [i for i in range(1, n+1) if n % i == 0]
    return answer

# --------- input ------------
n = 24
print(solution(n))