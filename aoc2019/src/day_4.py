# range is 359282-820401
def check_double(num):
    output = False
    count = 1
    for i in range(1, len(num)):
        # check the edge case
        if i == len(num)-1 and num[i] == num[i-1] and num[i] != num[i-2]:
            output = True
        if num[i] == num[i-1]:
            count += 1
        elif num[i] != num[i-1] and count == 2:
            output = True
            break
        else:
            count=1
    if output:
        print(num)
    return output


def check_increasing(num):
    output = False
    num_copy = [a for a in num]
    num_copy.sort()
    if num_copy == num:
        output = True
    return output


def check_criteria(num):
    output = False
    if check_double(num) and check_increasing(num):
        output = True
    return output


bottom = 359282
top = 820401
count = 0
for i in range(bottom, top + 1):
    num_list = [int(x) for x in str(i)]
    if check_criteria(num_list):
        count += 1
print(count)

