# “Hi He Lied Because Boron Could Not Oxidize Fluorine.
#  New Nations Might Also Sign Peace Security Clause. Arthur King Can.”
# という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字,
# それ以外の単語は先頭の2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への
# 連想配列（辞書型もしくはマップ型）を作成せよ．

str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
one_ch = [1, 5, 6, 7, 8, 9, 15, 16, 19]
# 20220402 1346
dict = {idx: word[:1] if idx in one_ch else word[:2] for idx, word in enumerate(str.split(),start=1)}

print(dict)