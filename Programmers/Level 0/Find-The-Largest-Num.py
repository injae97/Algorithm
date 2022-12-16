def solution(array):
    return [max(array), array.index(max(array))]

# --------- input ------------
array = [1, 8, 3]
print(solution(array))