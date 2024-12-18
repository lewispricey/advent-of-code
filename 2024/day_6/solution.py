def read_data_file(file_name):
    with open(f"{file_name}.txt", "r") as file:
        return [line.strip() for line in file.readlines()]


class GuardTracker:
    def __init__(self):
        self.possible_moves = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}
        self.directions = {"^": "N", ">": "E", "V": "S", "<": "W"}
        self.guard_location = None
        self.guard_direction = None
        self.map = {}
        self.walls_hit = None

    def create_map(self, map_data):
        map = dict()

        for r, row in enumerate(map_data):
            for c, col in enumerate(row):
                if col in self.directions:
                    self.guard_location = (r, c)
                    self.guard_direction = self.directions[col]
                    map[(r, c)] = "x"
                else:
                    map[(r, c)] = col

        self.map = map
        self.walls_hit = []
        return map

    def move_guard(self):
        while True:
            next_step = self.get_next_step()

            if next_step not in self.map:
                return 0

            if self.map[next_step] == "#":
                if (self.guard_direction, *next_step) in self.walls_hit:
                    return 1
                else:
                    self.walls_hit.append((self.guard_direction, *next_step))
                    self.rotate_guard()
            else:
                self.guard_location = next_step
                self.map[next_step] = "x"

    def count_visited(self):
        final_map = list(self.map.values())
        return final_map.count("x")

    def rotate_guard(self):
        rotations = {"N": "E", "E": "S", "S": "W", "W": "N"}
        self.guard_direction = rotations[self.guard_direction]

    def get_next_step(self):
        return tuple(
            [
                self.possible_moves[self.guard_direction][i] + self.guard_location[i]
                for i in range(2)
            ]
        )

    def part_1(self, data):
        self.create_map(data)
        self.move_guard()
        return self.count_visited()

    def part_2(self, data):
        base_map = self.create_map(data)
        loops_found = 0

        for coord in base_map:
            print(coord)
            self.map = self.create_map(data)
            self.walls_hit = []

            if self.map[coord] != "#" and coord != self.guard_location:
                self.map[coord] = "#"
                loops_found += 1 if self.move_guard() else 0

        return loops_found


if __name__ == "__main__":
    data = read_data_file("full_data")

    guard_tracker = GuardTracker()
    part_1 = guard_tracker.part_1(data)
    part_2 = guard_tracker.part_2(data)

    print("part_1:", part_1)
    print("part_2:", part_2)
