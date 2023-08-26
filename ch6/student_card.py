class StudentCard:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def print_info(self):
        print(f"学籍番号: {self.id}")
        print(f"氏名: {self.name}")


if __name__ == "__main__":
    a = StudentCard(1234, "鈴木太郎")
    b = StudentCard(1235, "佐藤花子")

    a.print_info()
    b.print_info()
