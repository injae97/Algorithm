def solution(n):
    result = []
    for i in range(0,n + 1):
        if i % 2 == 0:
            continue
        else:
            result.append(i)

    return result

# --------- input ------------
n = 10
print(solution(n))