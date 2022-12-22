def solution(numbers):
    numbers.sort()
    return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2]))

# --------- input ------------
numbers = [0, -31, 24, 10, 1, 9]
print(solution(numbers))