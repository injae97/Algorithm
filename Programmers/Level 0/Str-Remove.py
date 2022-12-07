def solution(my_string, letter):
    string = ""
    for i in range(len(my_string)):
        if my_string[i] == letter:
            continue
        else:
            string += my_string[i]

    return string

def solution2(my_string, letter):
    return my_string.replace(letter, '')

# --------- input ------------
my_string = "abcdef"
letter = "f"
print(solution(my_string, letter))