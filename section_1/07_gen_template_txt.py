# 引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
# さらに，x=12, y=”気温”, z=22.4として，実行結果を確認せよ

# import sys
# args = sys.argv
# def gen_temp_txt():
#     print(f"{args[1]}時の{args[2]}は{args[3]}")
# gen_temp_txt()

def gen_temp_txt(x, y, z):
    print(f"{x}時は{y}は{z}")

gen_temp_txt("12","気温",22.4)
