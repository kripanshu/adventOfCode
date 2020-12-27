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
                    custom_forms.extend(list(line))
                    if line == "\n":
                        count += 1
                        self.update_group_details_part1(custom_forms)
                        custom_forms = []

                print("---end: part1 total : ", self.part1_total_count)
                print("---end: part2 total : ", self.part2_total_count)
            except Exception as e:
                print(e)

    def update_group_details_part1(self, custom_forms: List):
        """ filter list to avoid '\n' and create a set and get count not efficient enough but clean"""
        filtered_list = list(filter(lambda x: (x != "\n"), custom_forms))
        self.part1_total_count += len(set(filtered_list))


if __name__ == "__main__":
    obj = CustomCustoms()
    obj.run("input/day06_input.txt")
