prompt_word:

```markdown
请你使用python代码，完成下面这个需求。

1. 我现在需要在指定目录下生成约80个空文件，文件的格式名字如下:aaa-xxxx-cccc.pdf，其中a表示任意字符，xxxx表示一个店家的名字，c表示一个四位数的金额。
2. 上面的命令当中，xxxx所表示的店家名字可能会重复出现。

```

code:

```python
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
    target_directory = "your_target_directory"  # 替换为你想要的目录
    filenames = generate_filenames(80, store_names)
    create_files(filenames, target_directory)
```

这段Python代码将会在指定目录下生成80个空的PDF文件，文件名格式为"aaa-xxxx-cccc.pdf"。其中a表示任意字符，xxxx表示一个店家的名字（从给定的store_names列表中选择），c表示一个四位数的金额。

请注意，为了测试这段代码，你需要在指定的目录下具有创建文件的权限。确保将变量`target_directory`替换为你希望在其中生成这些文件的目录。