# withステートメントを使用することで、closeを書かなくても、withのインデント内の処理が実行されたらcloseされるようになる。

# openでファイルを開くとくは、withが大事
with open("test.txt","w") as f :
    f.write("Test\n")
    print("02-with-statement",file=f)