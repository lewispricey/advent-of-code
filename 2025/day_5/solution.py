from utils.read_txt import read_txt


class FreshIngredientFinder:
    def __init__(self, ranges, instructions):
        self.ranges = ranges
        self.instructions = [int(instruction) for instruction in instructions]
        self.possible_fresh_ids = set()
        self.fresh_ingredient_count = 0

    def create_fresh_id_range(self):
        for r in self.ranges:
            start_end = r.split("-")
            start = int(start_end[0])
            end = int(start_end[1])

            range_values = [i for i in range(start, end + 1)]
            self.possible_fresh_ids.update(range_values)

    def check_id_in_range(self, id):
        return id in self.possible_fresh_ids

    def process_instructions(self):
        for instruction in self.instructions:
            if self.check_id_in_range(instruction):
                self.fresh_ingredient_count += 1


def get_fresh_ingredient_count(ranges, instructions):
    # read lines one at a time
    pass


def split_input_data(data):
    line_break_index = data.index("")
    ranges = data[:line_break_index]
    instructions = data[line_break_index + 1 :]

    with open("full_ranges.txt", "w") as f:
        for r in ranges:
            f.write(r + "\n")

    with open("full_instructions.txt", "w") as f:
        for instr in instructions:
            f.write(instr + "\n")


def part_1():
    fresh_ingredient_counter = 0
    with open("full_instructions.txt", "r") as ingredients_file:
        for ingredient_str in ingredients_file:
            ingrediant_id = int(ingredient_str.strip())

            with open("full_ranges.txt", "r") as ranges_file:
                for range_str in ranges_file:
                    start_end = range_str.strip().split("-")
                    start = int(start_end[0])
                    end = int(start_end[1])

                    if start <= ingrediant_id <= end:
                        fresh_ingredient_counter += 1
                        break

    return fresh_ingredient_counter


def check_overlap(range1_start, range2_start, range1_end, range2_end):
    return range1_start < range2_end and range2_start <= range1_end


def part_2():
    # part 2 collapse the ranges by looping over them checking them for overlaps and merging them until no more overlaps exist
    # take the final ranges, and minus the end from the start to get the total number of fresh ids
    data = read_txt("full_ranges.txt")
    ranges = []

    for range_str in data:
        start_end = range_str.strip().split("-")
        start = int(start_end[0])
        end = int(start_end[1])
        ranges.append((start, end))

    print(ranges)


if __name__ == "__main__":
    data = read_txt("full_data.txt")
    split_input_data(data)
    result = part_1()
    print("part_1:", result)
    result = part_2()
    print("part_2:", result)
    # print(line_break_index, ranges, instructions)

    # cafeteria = FreshIngredientFinder(ranges, instructions)
    # cafeteria.create_fresh_id_range()
    # print(len(cafeteria.possible_fresh_ids))
    # cafeteria.process_instructions()

    # print(cafeteria.fresh_ingredient_count)
