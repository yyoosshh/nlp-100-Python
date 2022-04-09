# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ
# この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．

def ngram(n, lst):
    return list(zip(*[lst[i:] for i in range(n)]))

str = "I am an NLPer"
words_bi_gram = ngram(2, str.split())
char_bi_gram = ngram(2, str)

print('単語', words_bi_gram)
print('文字', char_bi_gram)
