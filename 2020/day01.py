import re
from input.day01_input import input_data
target = 2020
data = re.findall(r'\d+', input_data)
test_list = [int(i) for i in data]


def first_helper():
    # part1
    # return two_sum(target, )
    # part2
    return three_sum(test_list, len(test_list), target)


def two_sum(n_target, temp):
    a, b = 0, 0
    for key, _ in temp.items():
        k = n_target - key
        if k in temp:
            print(k, key, n_target)
            a, b = key, k
            break
    # print(n_target, a, b)
    return a, b


def three_sum(A, arr_size, sum):
    for i in range(0, arr_size - 1):
        # Find pair in subarray A[i + 1..n-1]
        # with sum equal to sum - A[i]
        s = set()
        curr_sum = sum - A[i]
        for j in range(i + 1, arr_size):
            if (curr_sum - A[j]) in s:
                return A[i] * A[j] * (curr_sum - A[j])
            s.add(A[j])

    return 0
