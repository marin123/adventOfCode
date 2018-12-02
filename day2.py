def get_two_and_three(input):
    dictionary_count={}
    is_two_letters = 0
    is_three_letters = 0
    for letter in input:
        if letter in dictionary_count:
            current_value = dictionary_count[letter]
            dictionary_count[letter] = current_value+1
        else:
            dictionary_count[letter] = 1
    print(dictionary_count.values())
    for values in dictionary_count.values():
        if 2 == values:
            is_two_letters = 1
        if 3 == values:
            is_three_letters = 1
    return is_two_letters, is_three_letters



f = open("input_day_2.txt", "r")
output = 0
count_two_letters = 0
count_three_letters = 0
for line in f:
    count_two_letters_inc, count_three_letters_inc = get_two_and_three(line)
    count_two_letters += count_two_letters_inc
    count_three_letters += count_three_letters_inc
print(count_two_letters*count_three_letters)



# print(is_three_letters("aabbs"))
# print(is_two_letters("aa"))
