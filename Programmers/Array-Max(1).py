def solution(numbers):
    numbers.sort(reverse=True)
    return numbers[0] * numbers[1]

# --------- input ------------
numbers = [1, 2, 3, 4, 5]
print(solution(numbers))