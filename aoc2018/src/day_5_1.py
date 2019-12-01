f=open('input_day_5.txt', "r")
test_string = f.readline() + ' '
#test_string = 'dabAcCaCBAcCcaDA '
new_string=''
i=0
explosion_count = 1
while explosion_count != 0:
    explosion_count=0
    while i < len(test_string)-1:
        letter = test_string[i]
        letter_next = test_string[i+1]
        if letter != letter_next and letter.upper() == letter_next.upper():
            print("explode")
            explosion_count += 1
            i += 2
        else:
            new_string = new_string + letter
            i += 1
    test_string = ''
    print(len(new_string), new_string)
    new_string = new_string + ' '
    i = 0
    while i < len(new_string)-1:
        letter = new_string[i]
        letter_next = new_string[i+1]
        if letter != letter_next and letter.upper() == letter_next.upper():
            print("explode")
            explosion_count += 1
            i += 2
        else:
            test_string = test_string + letter
            i += 1
    print(len(test_string), test_string)
    test_string = test_string + ' '


    new_string = ''
    i = 0
