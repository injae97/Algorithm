def solution(num_list):
    return num_list[::-1]

def solution2(num_list):
    num_list.reverse()
    return num_list

# --------- input ------------
num_list = [1, 2, 3, 4, 5]
print(solution(num_list))