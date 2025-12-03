from utils.read_txt import read_txt


def get_largest_possible_number(num_str, required_length):
    start_index = 0
    result = ""

    for i in range(required_length, 0, -1):
        stop_index = len(num_str) - i + 1
        availible_digits = num_str[start_index:stop_index]

        largest_digit = max(availible_digits)
        largest_digit_index = availible_digits.index(largest_digit) + start_index
        start_index = largest_digit_index + 1

        result += largest_digit

    return int(result)


if __name__ == "__main__":
    data = read_txt("full_data.txt")

    highest_number_pairs = [get_largest_possible_number(row, 2) for row in data]
    sum_of_highest_number_pairs = sum(highest_number_pairs)
    print("part_1:", sum_of_highest_number_pairs)

    highest_12_digit_nums = [get_largest_possible_number(row, 12) for row in data]
    sum_of_highest_12_digit_nums = sum(highest_12_digit_nums)
    print("part_2:", sum_of_highest_12_digit_nums)
