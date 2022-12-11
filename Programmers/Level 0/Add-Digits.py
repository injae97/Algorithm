def solution(n):
    result = 0
    n = list(map(int, str(n))) # 1234 -> [1, 2, 3, 4]
    for i in range(len(n)):
        result += n[i]

    return result

def solution2(n):
    return sum(list(map(int, str(n))))

def solution3(n):
    return sum(int(i) for i in str(n))

def solution4(n):
    answer = 0
    while n:
        answer += n % 10 # 1234 -> 4, 123 -> 3, 12 -> 2, 1 -> 1 value save
        n //= 10 # 1234 -> 123, 123 -> 12, 12 -> 1
        print(n)

    return answer
# --------- input ------------
n = 1234
print(solution4(n))