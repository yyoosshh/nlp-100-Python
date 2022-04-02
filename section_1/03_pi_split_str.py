# “Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”
# という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
import re

str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

# 20220402 1303
# word_lst = [len(word.strip(',.')) for word in str.split()]
# 20220402 1311
word_lst = [len(re.sub("[.,]","", word)) for word in str.split()]

print(word_lst)
# [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]