def solution(my_string, n):
    string = ""
    for i in range(len(my_string)):
        string += my_string[i] * n

    return string

def solution2(my_string, n):
    return ''.join(i*n for i in my_string)

# --------- input ------------
my_string = "hello"
n = 3
print(solution(my_string, n))