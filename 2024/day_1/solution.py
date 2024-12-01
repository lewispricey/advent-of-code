def read_data_file(file_name):
    with open(f"{file_name}.txt", "r") as file:
        return file.read()


def format_input(data_set):
    left_list = []
    right_list = []

    rows = data_set.split("\n")

    for i in range(len(rows) - 1):
        split_digits = rows[i].split("   ")
        left_list.append(int(split_digits[0]))
        right_list.append(int(split_digits[1]))

    return (left_list, right_list)


def calculate_row_differences(l, r):
    l.sort()
    r.sort()
    differences = [max(l[i] - r[i], r[i] - l[i]) for i in range(len(l))]

    return sum(differences)


def calulcate_occourences(left, right):
    return sum([item * right.count(item) for item in left])


if __name__ == "__main__":
    data_set = read_data_file("full-data")
    left_list, right_list = format_input(data_set)

    part1_total = calculate_row_differences(left_list, right_list)
    part2_total = calulcate_occourences(left_list, right_list)

    print("part1:", part1_total)
    print("part2:", part2_total)
