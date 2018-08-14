# -*- coding: utf-8 -*-

# 引数を受け取る
import sys
args = sys.argv

# 引数チェック
if len(args) != 2 or not args[1]:
  s = "吾輩は猫である"
  print("引数が不正なためサンプルとして [ " + s + " ] を使用します")
else:
  s = args[1]
  print("[ " + s + " ] を使用します")

# 形態素解析
from janome.tokenizer import Tokenizer
t = Tokenizer()

# リストに追加
def add_list(key, list):
  if len(list) > 0:
    exist_no = None
    for i, item in enumerate(list):
      if item[0] is key:
        exist_no = i
    if exist_no is not None:
      list[exist_no][1] += 1
    else:
      list.append([key, 1])  
  else:
    list.append([key, 1])

# 名詞リスト作成
# print(' --- 名詞リスト作成 --- ')
noun_list = []
for token in t.tokenize(s):
  # print(token)
  str_surface = token.surface
  str_type = token.part_of_speech.split(',')[0]
  if str_type == u'名詞':
    add_list(str_surface, noun_list)

# 結果表示
print(' --- 結果表示 --- ')
from operator import itemgetter
noun_list.sort(key=itemgetter(1))
noun_list.reverse()
for item in noun_list:
  print(item)