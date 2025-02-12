import json

# json式で書き込むにはdump()を使用する。
data = [{"id":1},{"id":2}]
fp = open("sample.json","w")
json.dump(data,fp)
fp.close

# jsonはloadで読み込む
fp = open("sample.json")
s = json.load(fp)
print(s)