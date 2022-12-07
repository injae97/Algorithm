def solution(numbers):
    temp = 0
    for i in range(len(numbers)):
        temp += numbers[i]

    result = temp / len(numbers)
    return result

def solution2(numbers):
    result = sum(numbers) / len(numbers)
    return result

# --------- input ------------
numbers = [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
print(solution(numbers))