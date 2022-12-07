def solution(my_string, letter):

    temp = ""
    for i in range(len(my_string)):
        if my_string[i] == letter:
            continue
        else:
            temp += my_string[i]

    return temp

# --------- input ------------
my_string = "abcdef"
letter = "f"
print(solution(my_string, letter))