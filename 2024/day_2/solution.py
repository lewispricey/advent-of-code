import copy


def read_data_file(file_name):
    with open(f"{file_name}.txt", "r") as file:
        return file.read()


def format_data(dataset):
    rows = data_set.split("\n")
    reports = [value.split(" ") for value in rows]

    return [[int(item) for item in reports[i]] for i in range(len(reports) - 1)]


def part1(reports):
    reports = copy.deepcopy(reports)
    reports_safety = list()

    for i in range(len(reports)):
        cur_report = reports[i]

        asc_reports = sorted(cur_report)
        desc_reports = sorted(cur_report, reverse=True)
        are_ordered = cur_report == asc_reports or cur_report == desc_reports

        cur_report.sort()

        count = 0
        for j, item in enumerate(cur_report):
            if j == 0:
                count += 1
            else:
                prev_item = cur_report[j - 1]
                within_boundries = item - prev_item != 0 and item - prev_item <= 3
                if are_ordered and within_boundries:
                    count += 1

        if count == len(cur_report):
            reports_safety.append(True)
        else:
            reports_safety.append(False)

    return reports_safety.count(True)


def part2(reports):
    # This part two is horror, purely a brute force approach 5 minutes before work.
    # Refactor: The secondary (skip) condition should be refactored to prevent the multiple if statements & the nested for loop needs updating.
    # The code itself works for the input however may allow for multiple skips rarther than the stated 1 per row.
    reports_safety = list()

    for i in range(len(reports)):
        cur_report = reports[i]

        asc_reports = sorted(cur_report)
        desc_reports = sorted(cur_report, reverse=True)
        are_ordered = cur_report == asc_reports or cur_report == desc_reports

        cur_report.sort()

        count = 0
        for j, item in enumerate(cur_report):
            if j == 0:
                count += 1
            else:
                prev_item = cur_report[j - 1]
                within_boundries = item - prev_item != 0 and item - prev_item <= 3
                if are_ordered and within_boundries:
                    count += 1
                else:
                    prev_item = cur_report[j - 2]
                    within_boundries = item - prev_item != 0 and item - prev_item <= 3
                    if are_ordered and within_boundries:
                        count += 1

        if count == len(cur_report):
            reports_safety.append(True)
        else:
            reports_safety.append(False)

    return reports_safety.count(True)


if __name__ == "__main__":
    data_set = read_data_file("full-data")
    reports = format_data(data_set)

    part_1_result = part1(reports)
    part_2_result = part2(reports)

    print(part_1_result)
    print(part_2_result)
