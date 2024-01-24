from pathlib import Path
import random
import string
import sys


def create_random_string(length):
    """指定された長さのランダムな文字列を生成する関数"""
    letters = string.ascii_letters + string.digits
    return "".join(random.choice(letters) for i in range(length))


def create_files(num_files, file_size, directory="test_files"):
    """指定された数とサイズのファイルを生成する関数"""
    Path(directory).mkdir(parents=True, exist_ok=True)

    for i in range(num_files):
        filename = f"{directory}/file_{i}.txt"
        with open(filename, "w") as f:
            f.write(create_random_string(file_size))


# このファイルが直接実行された場合（テスト用）
# win: Measure-Command{ python tasks_file.py 100 1048576}
# mac: time python tasks_file.py 100 1048576
if __name__ == "__main__":
    num_files = int(sys.argv[1])
    file_size = int(sys.argv[2])

    create_files(num_files, file_size)
