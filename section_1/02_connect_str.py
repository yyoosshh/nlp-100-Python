# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

car_patrol_str = "パトカー"
car_taxi_str = "タクシー"

ans_str = ''.join([i + j for i, j in zip(car_patrol_str, car_taxi_str)])

print(ans_str)