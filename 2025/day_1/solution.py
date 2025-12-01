from utils.read_txt import read_txt


class Safe:
    def __init__(self):
        self.dial_position = 50
        self.max_dial_position = 99
        self.zero_count = 0

    def turn_dial_left(self, steps):
        for _ in range(steps):
            self.dial_position -= 1

            if self.dial_position == 0:
                self.zero_count += 1
            elif self.dial_position < 0:
                self.dial_position = self.max_dial_position

    def turn_dial_right(self, steps):
        for _ in range(steps):
            self.dial_position += 1

            if self.dial_position > self.max_dial_position:
                self.dial_position = 0
                self.zero_count += 1


if __name__ == "__main__":
    data = read_txt("full_data.txt")

    safe = Safe()

    for line in data:
        direction = line[0]
        steps = int(line[1:])

        match direction:
            case "L":
                safe.turn_dial_left(steps)
            case "R":
                safe.turn_dial_right(steps)

    print(safe.zero_count)
