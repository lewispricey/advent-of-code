def read_data_file(file_name):
    with open(f"{file_name}.txt", "r") as file:
        return [line.strip() for line in file.readlines()]


def part_1(grid):
    counter = 0

    def count_contents(string):
        xmas_count = string.count("XMAS")
        samx_count = string.count("SAMX")
        return xmas_count + samx_count

    row_count = len(grid)
    col_count = len(grid[0])

    columns = ["".join([row[i] for row in grid]) for i in range(row_count)]

    combined_row_and_cols = ",".join([*grid, *columns])
    counter += count_contents(combined_row_and_cols)

    print("Count before diagonals", counter)

    left_diagonals = {}
    for row in range(row_count):
        for col in range(col_count):
            key = row - col
            if key not in left_diagonals:
                left_diagonals[key] = ""
            left_diagonals[key] += grid[row][col]

    right_diagonals = {}
    for row in range(row_count):
        for col in range(col_count):
            key = row + col
            if key not in right_diagonals:
                right_diagonals[key] = ""
            right_diagonals[key] += grid[row][col]

    combined_diagonal_values = [*left_diagonals.values(), *right_diagonals.values()]

    counter += count_contents(",".join(combined_diagonal_values))

    return counter


if __name__ == "__main__":
    data = read_data_file("test_data")
    # data = read_data_file("full_data")
    part_1_total = part_1(data)
    print("Part 1:", part_1_total)
