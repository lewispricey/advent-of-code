def read_txt(file_path):
    with open("full_data.txt", "r", encoding="utf-8") as f:
        data = f.read().strip().split("\n")

    return data
