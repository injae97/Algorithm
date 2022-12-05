def solution(sides):
    sides.sort()
    max_num = sides[-1]
    if max_num < sides[0] + sides[1]:
        return 1
    else :
        return 2

def solution2(sides):
    return 1 if max(sides) < (sum(sides) - max(sides)) else 2

# --------- input ------------
sides = [1, 2, 3]
print(solution(sides))