class Person(object):

    #オブジェクトで共有される変数
    #initで初期化しなくていいものを入れる（リストはやめといた方が良い）
    kind = "human"

    def __init__(self,name):
        # self.kind = "human"
        self.name = name

    def who_are_you(self):
        print(self.name, self.kind)

a = Person("A")
a.who_are_you()

b = Person("B")
b.who_are_you()