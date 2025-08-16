class FileWordCounter:
    def __init__(self, file_path):
        self.file_path = file_path

    def total_words(self):
        with open(self.file_path, "r", encoding="utf-8") as f:
            text = f.read()
            word_count = len(text.split())
            print(f"Number of words in the file: {word_count}")


def run():
    counter = FileWordCounter("demo.txt")
    counter.total_words()

if __name__ == "__main__":
    run()
