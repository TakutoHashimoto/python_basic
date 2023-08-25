class StudentCard:
    def __init__(self, id, name):
        # インスタンス変数の変数名の先頭に__をつけると、クラスの外からはその変数にアクセスできなくなる
        self.__id = id
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__id


a = StudentCard(12345, "鈴木太郎")
# 以下2つの命令文はエラーになる
# print(a.__id)
# print(a.__name)

print(a.get_id())
print(a.get_name())
