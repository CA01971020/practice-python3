seat = []
min = 0
max = 3

bl = min <= len(seat) < max #seatがmaxより小さく、minより大きいとtrue
print(bl)

seat.append("p") #seatにpを追加

bl = min <= len(seat) < max
print(bl)
print(len(seat)) #配列に要素がどれくらい含まれているか確認

seat.append("p") #配列に2個目の要素として追加

bl = min <= len(seat) < max
print(bl)
print(len(seat))

seat.append("p")#配列に2個目の要素として追加

bl = min <= len(seat) < max
print(bl)
print(len(seat))

seat.pop(0)
bl = min <= len(seat) < max
print(bl)
print(len(seat))