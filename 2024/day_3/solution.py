import re


def read_data_file(file_name):
    with open(f"{file_name}.txt", "r") as file:
        return file.read()


def part_1_extract_pairs(currupted_mem):
    regex = r"(?<=mul\()\d+,\d+(?=\))"
    invocations = re.findall(regex, currupted_mem)
    return [tuple(int(num) for num in pair.split(",")) for pair in invocations]


if __name__ == "__main__":
    file_data = read_data_file("full-data")
    pairs = part_1_extract_pairs(file_data)
    multiplication_totals = [pair[0] * pair[1] for pair in pairs]

    print(sum(multiplication_totals))
