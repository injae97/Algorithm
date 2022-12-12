def solution(array):
    array.sort() # ASC : [-1, 0, 9]
    idx = len(array) // 2
    return array[idx]

# --------- input ------------
array = [9, -1, 0]
print(solution(array))