import re
data = [x for x in open('input.txt').read().splitlines()]

def valid_passwords(password_data):
    valid_passwords_count = 0
    for line in password_data:
        elements = re.findall(r"[\w']+", line)
        first_num = int(elements[0])
        second_num = int(elements[1])
        character = elements[2]
        password = elements[3]
        counter = password.count(character)
        if counter >= first_num and counter <= second_num:
            valid_passwords_count += 1
    return valid_passwords_count


def valid_passwords_2(password_data):
    valid_passwords_count = 0
    for line in password_data:
        elements = re.findall(r"[\w']+", line)
        first_num = int(elements[0])
        second_num = int(elements[1])
        character = elements[2]
        password = elements[3]
        counter = password.count(character)

        first_letter = password[first_num-1] == character
        second_letter = password[second_num-1] == character

        if (first_letter and not second_letter) or (not first_letter and second_letter):
            valid_passwords_count += 1
    return valid_passwords_count


def solution_part_1():
    return valid_passwords(data)


def solution_part_2():
    return valid_passwords_2(data)


if __name__ == "__main__":
    print(data[1])
    print("Answer Part 1:", solution_part_1())
    print("Answer Part 2:", solution_part_2())