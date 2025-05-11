class Person(object):
    
    # personの中でグローバルな変数
    kind = "human"

    # オブジェクトならアクセスできる
    def __init__(self):
        self.x = 100

    # オブジェクトとして生成されていなくても利用できるようにする
    @classmethod
    def what_is_your_kind(cls):
        return cls.kind
    
    # クラスの外でもいいが、この例の場合、humanのaboutなので、どこに関連する変数かわかりやすくできる
    @staticmethod
    def about(year):
        print("about human {}".format(year))

print("--------")

# オブジェクト
a = Person()
print(a.x)
# クラス
b = Person
# エラーになる
# print(b.x)
# kindにはアクセスされる
print(b.kind)

print("--------")

print(a.what_is_your_kind())
# オブジェクトではないのでエラーになる
print(b.what_is_your_kind)

print("---classmethod---")

print(Person.kind)
print(b.what_is_your_kind())

print("---staticmethod---")

Person.about(1999)