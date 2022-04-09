# “paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め,
# XとYの和集合，積集合，差集合を求めよ．さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ.

def ngram(n, lst):
    return set(zip(*[lst[i:] for i in range(n)]))

str_X = ngram(2,"paraparaparadise")
str_Y = ngram(2,"paragraph")

s_union = str_X | str_Y
s_intersection = str_X & str_Y
s_difference = str_X - str_Y

print("union:", s_union)
print("intersection:",s_intersection)
print("difference:",s_difference)
print({('s','e')} <= str_X)
print({('s','e')} <= str_Y)