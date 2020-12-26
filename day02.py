import re

real_data = open('input/day02_input.txt').readlines()


def second_helper():
    total = 0
    for data in real_data:
        a, b, c = data.split(" ")
        _min, _max = re.findall(r'\d+', a)
        char = re.findall(r'\w', b)[0]
        password = c.strip()

        # part 1
        #  count = 0
        # for c in password:
        #   if c == char:
        #     count+=1

        # if int(_min) <= count <= int(_max):
        #   total+=1

        # part 2
        pos1, pos2 = int(_min) - 1, int(_max) - 1
        if (password[pos1] == char) is not (password[pos2] == char):
            total += 1
    return total
