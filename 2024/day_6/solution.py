def read_data_file(file_name):
    with open(f"{file_name}.txt", "r") as file:
        return [line.strip() for line in file.readlines()]


class GuardTracker:
    def __init__(self):
        self.guard_location = None
        self.guard_direction = None
        self.map = {}

    def create_map(self, map_data):
        map = dict()

        directions = {"^": "N", ">": "E", "V": "S", "<": "W"}

        for r, row in enumerate(map_data):
            for c, col in enumerate(row):
                if col in directions:
                    self.guard_location = (r, c)
                    self.guard_direction = directions[col]
                    map[(r, c)] = "x"
                else:
                    map[(r, c)] = col

        self.map = map
        return map

    def move_guard(self):
        moves = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}
        count = 0
        while count < 1000000:
            count += 1
            next_step = tuple(
                [
                    moves[self.guard_direction][i] + self.guard_location[i]
                    for i in range(2)
                ]
            )

            if next_step not in self.map:
                break

            # check if its a hash and roate 90 clock
            if self.map[next_step] == "#":
                rotations = {"N": "E", "E": "S", "S": "W", "W": "N"}
                self.guard_direction = rotations[self.guard_direction]

            else:
                self.guard_location = next_step
                self.map[next_step] = "x"
            # else mark square and update guard position
        return count

    def count_visited(self):
        final_map = list(self.map.values())
        return final_map.count("x")

    def part_1(self, data):
        self.create_map(data)
        self.move_guard()
        return self.count_visited()

    def part_2(self, data):
        self.guard_location = None
        self.guard_direction = None
        # create a new map
        start_map = self.create_map(data)
        infinite_count = 0

        # loop through the keys
        for coord in start_map:
            print(coord)
            # create new map
            self.map = self.create_map(data)
            # update each key to be a new object if not currently an object and not guard location

            if self.map[coord] != "#" and coord != self.guard_location:
                self.map[coord] = "#"
                loop_count = self.move_guard()
                if loop_count == 1000000:
                    infinite_count += 1

        return infinite_count


# best solution!!!?
# just keep track of what wall has been hit at what angle, if the same wall is hit at the same angle then we've been there before

if __name__ == "__main__":
    data = read_data_file("full_data")

    guard_tracker = GuardTracker()
    part_1 = guard_tracker.part_1(data)
    part_2 = guard_tracker.part_2(data)
    print(part_1)
    print(part_2)
