def solution(n, numlist):
    answer = []
    for i in range(len(numlist)):
        if numlist[i] % n == 0:
            answer.append(numlist[i])

    return answer

def solution2(n, numlist):
    answer = [numlist[i] for i in range(len(numlist)) if numlist[i] % n == 0]
    return answer

# --------- input ------------
n = 3
numlist = [4, 5, 6, 7, 8, 9, 10, 11, 12]
print(solution(n, numlist))