def solution(my_string, n):
    string = ""
    for i in range(len(my_string)):
        string += my_string[i] * n

    return string

# --------- input ------------
my_string = "hello"
n = 3
print(solution(my_string, n))