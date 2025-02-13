class Human:
    # クラス変数human_nameとして"Takeshi"を定義
    human_name:str = "Takeshi"

    # クラス変数を変更するインスタンスを作成
    def change_name(self, human_name):
        Human.human_name = human_name

first_human = Human()
second_human = Human()

# 両方"Takeshi"が出力される。
print(first_human.human_name)
print(second_human.human_name)

# first_humanを"Jiro"に変更する
first_human.change_name("Jiro")
print("-------------")

# 両方"Jiro"になってしまう。
print(first_human.human_name)
print(second_human.human_name)

print("-------------")

class Human:
    def __init__(self, human_name:str="Takeshi"):  # 初期値を設定
        self.human_name = human_name  # インスタンス変数として定義

    def change_name(self, human_name):
        self.human_name = human_name  # インスタンス変数を変更

human1 = Human()
human2 = Human()
print(human1.human_name)  # Takeshi
human1.change_name("Jiro")  # human1 だけ変更
print(human2.human_name)  # Takeshi（human2 には影響しない！）

print("-------------")

human1 = Human()
print(human1.human_name)  # "Takeshi"

human1.change_name("Jiro")  # human1 の human_name を変更
print(human1.human_name)  # "Jiro" に上書きされる！
