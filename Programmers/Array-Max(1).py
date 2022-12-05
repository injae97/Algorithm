def solution(numbers):
    numbers.sort(reverse=True) # numbers = sorted(numbers, reverse=True) : 변수에 역순으로 정렬 후 할당
    return numbers[0] * numbers[1]

# --------- input ------------
numbers = [1, 2, 3, 4, 5]
print(solution(numbers))