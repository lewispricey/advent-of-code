import re


def read_data_file(file_name):
    with open(f"{file_name}.txt", "r") as file:
        return file.read()


def sum_multiplication_pairs(pairs):
    return sum([pair[0] * pair[1] for pair in pairs])


def part_1_extract_pairs(currupted_mem):
    regex = r"(?<=mul\()\d+,\d+(?=\))"
    invocation_args = re.findall(regex, currupted_mem)
    return [tuple(int(num) for num in pair.split(",")) for pair in invocation_args]


def part_2_extract_pairs(currupted_mem):
    regex = r"(?<=mul\()\d+,\d+(?=\))|do\(\)|don't\(\)"
    extracted_instructions = re.findall(regex, currupted_mem)

    pairs = list()

    execute = True
    for element in extracted_instructions:
        if element == "don't()":
            execute = False
            continue

        elif element == "do()":
            execute = True
            continue

        elif execute:
            pairs.append(tuple(int(num) for num in element.split(",")))

    return pairs


if __name__ == "__main__":
    file_data = read_data_file("full-data")

    part_1_pairs = part_1_extract_pairs(file_data)
    part_2_pairs = part_2_extract_pairs(file_data)

    print("part 1:", sum_multiplication_pairs(part_1_pairs))
    print("part 2:", sum_multiplication_pairs(part_2_pairs))
