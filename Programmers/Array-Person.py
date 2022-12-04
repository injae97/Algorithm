def solution(array, height):
    result = 0
    for i in range(len(array)):
        if height < array[i]:
            result += 1
        else:
            continue
    return result

def solution2(array, height):
    array.append(height)
    array.sort(reverse=True) # 역순으로 값 정렬 [192, 180, 170, 167, 149]
    return array.index(height)
# --------- input ------------
array = [149, 180, 192, 170]
height = 167
print(solution(array, height))