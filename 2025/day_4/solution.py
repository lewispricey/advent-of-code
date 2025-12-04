from utils.read_txt import read_txt

if __name__ == "__main__":
    data = read_txt("full_data.txt")

    mapping = {i: {j: col for j, col in enumerate(row)} for i, row in enumerate(data)}

    grid = [list(row) for row in data]

    neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    total_count = 0
    for row_index, row in enumerate(grid):
        for item_index, item in enumerate(row):
            if item != "@":
                continue

            roll_count = 0

            for x, y in neighbours:
                new_row = row_index + x
                new_item = item_index + y

                if new_row < 0 or new_item < 0:
                    continue

                try:
                    neighbour_value = grid[new_row][new_item]
                    if neighbour_value == "@":
                        roll_count += 1

                except IndexError:
                    continue

            if roll_count < 4:
                total_count += 1

    print("part_1:", total_count)
# recursive solition instead of nested loops?? - part2 recurse invoking with the grid until toilet paper count is zero ie return count + recurse_grid(new_grid)
