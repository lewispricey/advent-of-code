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

    left_diagonals = {}
    right_diagonals = {}

    for row in range(row_count):
        for col in range(col_count):
            left_key = row - col
            if left_key not in left_diagonals:
                left_diagonals[left_key] = ""
            left_diagonals[left_key] += grid[row][col]

            right_key = row + col
            if right_key not in right_diagonals:
                right_diagonals[right_key] = ""
            right_diagonals[right_key] += grid[row][col]

    combined_diagonal_values = [*left_diagonals.values(), *right_diagonals.values()]

    counter += count_contents(",".join(combined_diagonal_values))

    return counter


def part_2(grid):
    row_count = len(grid)
    col_count = len(grid[0])

    found_count = 0

    valid_patterns = ["SAM", "MAS"]

    for row in range(row_count):
        for column in range(col_count):
            current_char = grid[row][column]

            if current_char != "A":
                continue

            row_bounds = row - 1 >= 0 and row + 1 < row_count
            col_bounds = column - 1 >= 0 and column + 1 < col_count

            if not row_bounds or not col_bounds:
                continue

            left_diagonal = (
                grid[row - 1][column - 1] + current_char + grid[row + 1][column + 1]
            )

            right_diagonal = (
                grid[row - 1][column + 1] + current_char + grid[row + 1][column - 1]
            )
            is_valid = all(
                [
                    left_diagonal in valid_patterns,
                    right_diagonal in valid_patterns,
                ]
            )

            if is_valid:
                found_count += 1

    return found_count


if __name__ == "__main__":
    data = read_data_file("full_data")

    part_1_total = part_1(data)
    part_2_total = part_2(data)

    print("Part 1:", part_1_total)
    print("Part 2:", part_2_total)
