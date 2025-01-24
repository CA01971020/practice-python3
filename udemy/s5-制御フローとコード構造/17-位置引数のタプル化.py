# 関数の引数にargsを使用すると、入力値をタプルにまとめてくれる

## 一文字目はwordとして出力して、二文字目からはargsでタプルとして出力させることもできる
def test_func(word,*args):
    print("word=",word)
    ## for文でarg変数にargsを格納
    for arg in args:
        print(arg)

test_func("test!","tee","tssss")