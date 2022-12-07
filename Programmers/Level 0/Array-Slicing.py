def solution(numbers, num1, num2):
    return numbers[num1:num2 + 1]

# --------- input ------------
numbers = [1, 2, 3, 4, 5]
num1, num2 = 1, 3
print(solution(numbers, num1, num2))