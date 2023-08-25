class StudentCard:
    def __init__(self):
        print("初期化メソッド内の処理です")
        self.id = 0
        self.name = "未定"


a = StudentCard()
b = StudentCard()

a.id, a.name = 1234, "鈴木太郎"
b.id, b.name = 1235, "佐藤花子"
print(f"a.id: {a.id}, a.name: {a.name}")
print(f"b.id: {b.id}, b.name: {b.name}")
