def solution(cipher, code):
    answer = ""
    for i in range(code - 1, len(cipher), code):
        answer += cipher[i]

    return answer

def solution2(cipher, code):
    answer = cipher[code-1::code]
    return answer

# --------- input ------------
cipher = "dfjardstddetckdaccccdegk"
code = 4
print(solution2(cipher, code))