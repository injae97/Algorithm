def solution(num1, num2):
    if num1 == num2 :
        return 1
    elif num1 != num2 :
        return -1

def solution2(num1, num2):
    return 1 if num1 == num2 else -1

# --------- input ------------
num1, num2 = 2, 3
print(solution(num1, num2))