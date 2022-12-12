def solution(my_string):
    answer = list(map(str, str(my_string)))

    total = 0
    for i in range(len(answer)):
        if answer[i].isdigit():
            total += int(answer[i])

    return total

# --------- input ------------
my_string = "aAb1B2cC34oOp"
print(solution(my_string))
