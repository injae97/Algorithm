def solution(s1, s2):
    cnt = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                cnt += 1
            else:
                continue

    return cnt

def solution2(s1, s2):
    return len(set(s1)&set(s2)) # AND 연산자 이용

def solution3(s1, s2):
    cnt = 0
    for val in s1:
        if val in s2:  # val = a, b, c
            cnt += 1

    return cnt

# --------- input ------------
s1 = ["a", "b", "c"]
s2 = ["com", "b", "d", "p", "c"]
print(solution3(s1, s2))