class ReadWriteBend:
    def __init__(self, filename):
        self.filename = filename

    def save_text(self, text):
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(text)

    def load_text(self):
        with open(self.filename, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()

def run():
    handler = ReadWriteBend("demo.txt")
    handler.save_text("This file has a lot of good stories\n")
    print(handler.load_text())

if __name__ == "__main__":
    run()
