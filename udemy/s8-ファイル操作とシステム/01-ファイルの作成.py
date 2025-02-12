# w write=作成or更新
# a append=追加
# r 読み込み
f = open("test.txt","w")

# writeのほうが使われやすい
f.write("Test\n")

# printで書き込むことも可能
print("01-create-file",file=f)
print("My","name","is","Mike",sep="#",end="!",file=f)

# ファイルを作成して、書き込んだら、閉じる必要があるためcloseする
f.close()