def solution(numbers, direction):
    # pop keyword : Delete After Running
    if direction == 'right':
        numbers.insert(0, numbers.pop()) # pop() last index remove  e.g : [1, 2, 3] -> [1, 2]

    elif direction == 'left':
        numbers.append(numbers.pop(0)) # pop(0) first index remove  e.g : [1, 2, 3] -> [2, 3]

    return numbers

from collections import deque
def solution2(numbers, direction):
    numbers = deque(numbers)
    numbers.rotate(1 if direction == 'right' else -1) # deque([3, 1, 2])
    return list(numbers)

# --------- input ------------
numbers = [1, 2, 3]
direction = "right"
print(solution(numbers, direction))