with open ("test.txt","r") as f:
    print(f.tell())
    # 一文字読み込む
    print(f.read(1))
    # 5番目に移動する
    f.seek(5)
    print(f.read(1))
    f.seek(14)
    print(f.read(1))