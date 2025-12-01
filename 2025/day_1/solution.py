from utils.read_txt import read_txt


class Safe:
    def __init__(self, dial_start, max_dial_position=99):
        self.dial_position = dial_start
        self.max_dial_position = max_dial_position
        self.zero_count = 0

    def turn_dial(self, direction, steps):
        for _ in range(steps):
            if direction == "L":
                self.dial_position -= 1
                if self.dial_position < 0:
                    self.dial_position = self.max_dial_position
            elif direction == "R":
                self.dial_position += 1
                if self.dial_position > self.max_dial_position:
                    self.dial_position = 0

            if self.dial_position == 0:
                self.zero_count += 1


if __name__ == "__main__":
    data = read_txt("full_data.txt")

    safe = Safe(dial_start=50)

    for line in data:
        direction = line[0]
        steps = line[1:]
        safe.turn_dial(direction, int(steps))

    print(safe.zero_count)
