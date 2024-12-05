def read_data_file(file_name):
    with open(f"{file_name}.txt", "r") as file:
        return file.read()


def format_order_and_update(data):
    split_data = data.split("\n\n")

    order_data = split_data[0].split("\n")
    order_pairs = [[int(num) for num in order.split("|")] for order in order_data]

    updates_data = split_data[1].strip().split("\n")
    updates = [[int(num) for num in update.split(",")] for update in updates_data]

    return order_pairs, updates


class Page:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class Book:
    def __init__(self):
        self.front = None
        self.seen = set()

    def add_pages(self, before, after):
        # if no front create front and back, add before to front, append to seen
        if not self.front:
            return self.setup_initial_pair(before, after)
        #
        # if front = after create new page set current front to next on that new page instance and update front
        if self.front == after:
            new_front = Page(before, next=self.front)
            self.front.prev = new_front
            self.front = new_front
        # if front = before create Page with the
        #
        #
        pass

    def setup_initial_pair(self, before, after):
        self.seen.add(before)
        self.seen.add(after)
        second_page = Page(after)
        first_page = Page(before, next=second_page)
        second_page.prev = first_page
        self.front = first_page
        return

    def create_page(self, value, previous=None, next=None):
        # create new instance of a Page
        pass


def part_1():
    test = [47, 53]
    book = Book()
    book.add_pages(test[0], test[1])
    print(book.seen)
    print(book.front.value)


if __name__ == "__main__":
    raw_data = read_data_file("test_data")
    order_pairs, updates = format_order_and_update(raw_data)
    part_1()
    print(order_pairs, updates)
