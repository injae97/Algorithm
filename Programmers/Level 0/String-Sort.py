def solution(my_string):
    string = list(map(str, str(my_string)))
    answer = []
    for i in range(len(string)):
        if string[i].isdigit():
            answer.append(int(string[i]))

    answer.sort()
    return answer

# --------- input ------------
my_string = "hi12392"
print(solution(my_string))