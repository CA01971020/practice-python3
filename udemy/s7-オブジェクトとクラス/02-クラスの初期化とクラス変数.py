# Personクラス
class Person(object):
    # __init__はクラスが生成されたら最初に実行される
    def __init__(self,name):
        # self.name に 引数のnameを格納して出力
        self.name = name
        print(self.name)

    # selfは値を保持する役割を持つ
    def say_something(self):
        print("I am {}. hello".format(self.name))
        self.run(3)

    def run(self,num):
        print("num"*num)

    # デストラクタ
    def __del__(self):
        print("good bye")

person = Person("Mike")
person.say_something()

del person

print("#########")