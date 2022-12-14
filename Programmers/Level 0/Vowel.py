def solution(my_string):
    string = ""
    arr2 = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(my_string)):
        if my_string[i] in arr2: # How to use 'in' keyword? : if <string> in <list>
            continue
        else:
            string += my_string[i]

    return string

def solution2(my_string):
    vowels = ['a','e','i','o','u']
    for i in range(len(vowels)):
        my_string = my_string.replace(vowels[i], '')

    return my_string

# --------- input ------------
my_string = "nice to meet you"
print(solution2(my_string))