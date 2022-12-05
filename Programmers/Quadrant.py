def solution(dot):
    if dot[0] >= 1 and dot[1] >= 1:
        return 1
    elif dot[0] < 1 and dot[1] >= 1:
        return 2
    elif dot[0] < 1 and dot[1] < 1:
        return 3
    else :
        return 4

# --------- input ------------
dot = [2, 4]
print(solution(dot))