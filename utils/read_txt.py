def read_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = f.read().strip().split("\n")

    return data
