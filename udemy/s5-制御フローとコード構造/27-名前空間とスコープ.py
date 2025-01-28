# グローバルのanimal
animal = "cat"

def f():
    # ローカルのanimal
    animal = "dog"
    print(animal,locals())

## globalsで何が入っているのか確認できる
print(f(),globals())
