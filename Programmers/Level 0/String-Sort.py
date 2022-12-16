def solution(my_string):
    string = list(map(str, str(my_string)))
    answer = []
    for i in range(len(string)):
        if string[i].isdigit():
            answer.append(int(string[i]))

    answer.sort()
    return answer

def solution2(my_string):
    return sorted([int(my_string[i]) for i in range(len(my_string)) if my_string[i].isdigit()])

# --------- input ------------
my_string = "hi12392"
print(solution(my_string))