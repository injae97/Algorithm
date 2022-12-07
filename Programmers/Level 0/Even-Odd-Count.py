def solution(num_list):
    even, odd = 0, 0
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            even += 1
        else:
            odd += 1

    return [even, odd]

def solution2(num_list):
    result = [0, 0]
    for i in range(len(num_list)):
        result[num_list[i] % 2] += 1

    return result
# --------- input ------------
numbers = [1, 2, 3, 4, 5]
print(solution(numbers))