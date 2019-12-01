# test_string = 'dabAcCaCBAcCcaDA '
def explode(input_string):
    test_string_1 = input_string
    test_string = test_string_1
    new_string = ''
    i = 0
    explosion_count = 1
    while explosion_count != 0:
        explosion_count=0
        while i < len(test_string)-1:
            letter = test_string[i]
            letter_next = test_string[i+1]
            if letter != letter_next and letter.upper() == letter_next.upper():
                # print("explode")
                explosion_count += 1
                i += 2
            else:
                new_string = new_string + letter
                i += 1
        test_string = ''
        # print(len(new_string), new_string)
        new_string_cached = new_string
        new_string = new_string + ' '
        i = 0
        # print(explosion_count, "b")
        explosion_count = 0
        while i < len(new_string)-1:
            letter = new_string[i]
            letter_next = new_string[i+1]
            if letter != letter_next and letter.upper() == letter_next.upper():
                # print("explode")
                explosion_count += 1
                i += 2
            else:
                test_string = test_string + letter
                i += 1
        #print(explosion_count, len(test_string), test_string)
        test_string_cached = test_string
        test_string = test_string + ' '
        # print(explosion_count, "c", test_string)
        new_string = ''
        i=0
    if test_string_cached == None:
        return new_string_cached
    else:
        return test_string_cached


def remove_letter(input, char):
    clean_output = ''
    for letter in input:
        if char.upper() != letter.upper():
            clean_output = clean_output + letter
    return clean_output

lengths=[]
f = open('input_day_5.txt', "r")
test_string = f.readline() + ' '
for letter in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
    clean_input = remove_letter(test_string, letter)
    print(letter)
    lengths.append(len(explode(clean_input)))
    print(len(explode(clean_input)))
print(lengths)
# test_string = 'dabAcCaCBAcCcaDA '
