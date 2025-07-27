s = """\
AAA
BBB
CCC
DDD
"""

# w+は書き込みプラス読み込み
with open("test.txt","w+") as f :
    f.write(s)
    # seek0で戻る
    f.seek(0)
    print(f.read())

#r+はファイルが存在していれば書き込める
with open("test.txt","r+") as f :
    print(f.read())
    f.seek(0)
    f.write(s)