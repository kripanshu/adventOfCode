"""
Advent of code 2020 day 6
Sample input:
abc

a
b
c

ab
ac

a
a
a
a

b

Sample output
PART I:
3 + 3 + 3 + 1 + 1 = 11

PART II:
3 + 0 + 1 + 1 + 1 = 6
"""
from collections import defaultdict
from typing import List


class CustomCustoms:
    part1_total_count = 0
    part2_total_count = 0

    def run(self, path):
        custom_forms = []
        count = 0
        with open(path, 'r') as reader:
            try:
                line = True
                while line:
                    line = reader.readline()
                    if line != "\n":
                        custom_forms.extend(list(filter(lambda x: (x != "\n"), list(line))))
                        count += 1
                    else:
                        self.update_group_details_part1(custom_forms)
                        self.update_group_details_part2(custom_forms, count)
                        custom_forms = []
                        count = 0

                print("part1 total : ", self.part1_total_count)
                print("part2 total : ", self.part2_total_count)
            except Exception as e:
                print(e)

    def update_group_details_part2(self, custom_forms: List, count: int):
        """ filter list to avoid '\n' and create a set and get count not efficient enough but clean"""
        temp_count = 0
        my_dict = defaultdict(list)
        for item in custom_forms:
            my_dict[item].append("yes")

        for item, val in my_dict.items():
            if len(val) == count:
                temp_count += 1

        self.part2_total_count += temp_count

    def update_group_details_part1(self, custom_forms: List):
        """ filter list to avoid '\n' and create a set and get count not efficient enough but clean"""
        my_set = len(set(custom_forms))
        self.part1_total_count += my_set


if __name__ == "__main__":
    obj = CustomCustoms()
    obj.run("input/day06_input.txt")
