import re

inventory = open('input.txt').readlines()
max_so_far = -1
max_so_far_list = []
current_calories_per_elf = 0
for entry in inventory:
    if(entry != "\n"):
        current_calories_per_elf+= int(entry.strip("\n"))
    else:
        max_so_far_list.append(current_calories_per_elf)
        current_calories_per_elf = 0

    max_so_far = max(max_so_far, current_calories_per_elf)
    print("current_calories_per_elf: ",current_calories_per_elf, "max: ", max_so_far)

max_so_far_list.append(current_calories_per_elf)
max_so_far_list.sort(reverse=True)
total = max_so_far_list[0] + max_so_far_list[1] + max_so_far_list[2]

print(max_so_far_list, total)

