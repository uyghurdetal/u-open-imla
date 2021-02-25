import os
from shirkhan.string_tool import text_to_words

"""
处理文件句柄
"""


class File:
    def __init__(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(404, "给定文件没找到", file_path)
        self.path = file_path

    def get_lines(self, mode="r", encoding="utf-8"):
        file_lines = []
        with open(self.path, mode=mode, encoding=encoding) as f:
            file_lines = [line.strip() for line in f.readlines()]
        return file_lines

    @staticmethod
    def write_lines(file_path, lines=[], mode="w", encoding="utf-8", newline_separator="\n"):
        if lines is None or len(lines) == 0:
            return false
        with open(file_path, mode=mode, encoding=encoding) as target:
            for line in lines:
                line = line.strip()
                target.write(line)
                target.write(newline_separator)

    def get_text(self):
        return "".join(self.get_lines()).strip()

    def get_words(self):
        return self.get_text().split()

    def get_u_words(self):
        return text_to_words(self.get_text())

    def get_u_text(self):
        return " ".join(self.get_u_words()).strip()


if __name__ == '__main__':
    pass
    # fileHandler = File("test1.txt")
    # print(fileHandler.get_lines())
    # print(fileHandler.get_text())
    # print(fileHandler.get_words())
    # print(fileHandler.get_u_words())
