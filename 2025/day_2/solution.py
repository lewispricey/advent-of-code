import re

from utils.read_txt import read_txt


def check_half_sequence(number):
    stringified_number = str(number)
    test_left_str = stringified_number[0 : len(stringified_number) // 2]
    test_right_str = stringified_number[len(stringified_number) // 2 :]

    return test_left_str == test_right_str


def check_full_sequence(number):
    pattern = r"^(.+)\1+$"
    matches = re.findall(pattern, str(number))
    if matches:
        return True
    else:
        return False


def main(input_data):
    part_1_sequences = []
    part_2_sequences = []

    for start, stop in input_data:
        for i in range(start, stop):
            if check_half_sequence(i):
                part_1_sequences.append(i)
            if check_full_sequence(i):
                part_2_sequences.append(i)

    return sum(part_1_sequences), sum(part_2_sequences)


if __name__ == "__main__":
    raw_input = read_txt("full_data.txt")[0].split(",")

    data = [[int(value) for value in range_item.split("-")] for range_item in raw_input]

    result_1, result2 = main(data)

    print(f"Part 1: {result_1}")
    print(f"Part 2: {result2}")
