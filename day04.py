"""
Not a good code, bad use of global variables.

"""

import re

valid_passports = 0


def fourth_helper():
    passport = []
    count = 0
    with open('input/day04_input.txt', 'r') as reader:
        try:
            line = True
            while line:
                line = reader.readline()
                passport.extend(line.split(" "))
                if line == "\n":
                    count += 1
                    validate(passport)
                    passport = []

            print("---end: total : ", count)
            return valid_passports
        except Exception as e:
            print(e)


def validate(single_passport_data):
    global valid_passports
    required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    print("block -------- ")
    try:
        for item in single_passport_data:
            if len(item) > 1:
                key, value = item.split(":")
                if key.strip() == "byr":
                    if not validate_birth_year(value.strip()):
                        continue

                if key.strip() == "iyr":
                    if not validate_issue_year(value.strip()):
                        continue

                if key.strip() == "eyr":
                    if not validate_exp_year(value.strip()):
                        continue

                if key.strip() == "hgt":
                    if not validate_height(value.strip()):
                        continue

                if key.strip() == "hcl":
                    if not validate_hair(value.strip()):
                        continue

                if key.strip() == "ecl":
                    if not validate_eye(value.strip()):
                        continue

                if key.strip() == "pid":
                    if not validate_id(value.strip()):
                        continue

                if key.strip() in required_fields:
                    required_fields.remove(key.strip())

        if not len(required_fields):
            valid_passports += 1
        print("result - ", valid_passports)
        print("-------* block", "\n \n")
    except Exception as e:
        print(e)


def validate_birth_year(data):
    """
    four digits; at least 1920 and at most 2002.
    """
    try:
        if not (1920 <= int(data) <= 2002):
            return False
        return True
    except Exception as e:
        print(" returning False ....", e)
        return False


def validate_issue_year(data):
    """
    four digits; at least 2010 and at most 2020.
    """
    try:
        if not (2010 <= int(data) <= 2020):
            return False
        return True
    except Exception as e:
        print(" returning False ....", e)
        return False


def validate_exp_year(data):
    """
    four digits; at least 2020 and at most 2030.
    """
    try:
        if not (2020 <= int(data) <= 2030):
            return False
        return True
    except Exception as e:
        print(" returning False ....", e)
        return False


def validate_height(data):
    """
    a number followed by either cm or in:

      If cm, the number must be at least 150 and at most 193.
      If in, the number must be at least 59 and at most 76.

    """
    try:
        h = int(re.findall(r'\d+', data)[0])
        if "cm" in data:
            if not (150 <= h <= 193):
                return False
        elif "in" in data:
            if not (59 <= h <= 76):
                return False
        elif "cm" not in data or "in" not in data:
            return False
        return True
    except Exception as e:
        print(" returning False ....", e)
        return False


def validate_hair(data):
    """
    a # followed by exactly six characters 0-9 or a-f.
    """
    try:
        real_data = data[1:]
        if len(real_data) != 6:
            return False
        if not re.match(r'^[a-f0-9]*$', real_data):
            return False
        return True
    except Exception as e:
        print(" returning False ....", e)
        return False


def validate_eye(data):
    """
    exactly one of: amb blu brn gry grn hzl oth.
    """
    try:
        eye_color = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
        if data not in eye_color:
            return False
        return True
    except Exception as e:
        print(" returning False ....", e)
        return False


def validate_id(data):
    """
    a nine-digit number, including leading zeroes.
    """
    try:
        if len(data) != 9:
            return False
        return True
    except Exception as e:
        print(" returning False ....", e)
        return False
