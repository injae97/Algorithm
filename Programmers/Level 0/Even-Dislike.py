def solution(n):
    result = []
    for i in range(1, n+1):
        if i % 2 == 0:
            continue
        else:
            result.append(i)

    return result

def solution2(n):
    return [i for i in range(1, n+1) if i % 2 == 1]

def solution3(n):
    return [i for i in range(1, n+1, 2)]

# --------- input ------------
n = 10
print(solution2(n))