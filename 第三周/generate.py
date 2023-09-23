import os
import random
import string

def random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def random_number(length):
    return ''.join(random.choice(string.digits) for _ in range(length))

def generate_filenames(count, store_names, extension=".pdf"):
    filenames = []
    for _ in range(count):
        prefix = random_string(3)
        store_name = random.choice(store_names)
        amount = random_number(4)
        filename = f"{prefix}-{store_name}-{amount}{extension}"
        filenames.append(filename)
    return filenames

def create_files(filenames, directory="."):
    if not os.path.exists(directory):
        os.makedirs(directory)

    for filename in filenames:
        filepath = os.path.join(directory, filename)
        with open(filepath, "w") as f:
            pass

if __name__ == "__main__":
    store_names = ["store1", "store2", "store3", "store4", "store5"]
    target_directory = "file"  # 替换为你想要的目录
    filenames = generate_filenames(80, store_names)
    create_files(filenames, target_directory)