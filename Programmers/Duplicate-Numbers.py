def solution(array, n):
    cnt = 0
    for i in range(len(array)):
        if n == array[i]:
            cnt += 1

    answer = cnt
    return answer

# --------- input ------------
array = [1, 1, 2, 3, 4, 5]
n = 1
print(solution(array, n))