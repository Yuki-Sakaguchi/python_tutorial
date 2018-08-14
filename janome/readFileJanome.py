# -*- coding: utf-8 -*-

# 引数を受け取る
import sys
args = sys.argv

# 引数チェック
file_name = ""
if len(args) != 2 or not args[1]:
  file_name = "./sample/bocchan.txt"
  print("引数が不正なためサンプルとして [ " + file_name + " ] を使用します")
else:
  file_name = args[1]
  print("[ " + file_name + " ] を使用します")

# ファイルを受け取る
f = open(file_name)
s = f.read()
s = s.replace("\n", "") # 改行を削除
f.close()

# 形態素解析
from janome.tokenizer import Tokenizer
t = Tokenizer()

# リストに追加
def add_list(key, list, token):
  if len(list) > 0:
    exist_no = None
    for i, item in enumerate(list):
      if item[0] is key:
        exist_no = i
    if exist_no is not None:
      list[exist_no][1] += 1
    else:
      list.append([key, 1, token])  
  else:
    list.append([key, 1, token])

# 名詞リスト作成
# print(' --- 名詞リスト作成 --- ')
noun_list = []
for token in t.tokenize(s):
  # print(token)
  str_surface = token.surface
  str_type = token.part_of_speech.split(',')[0]
  if str_type == u'名詞':
    add_list(str_surface, noun_list, token)

# 結果表示
print(' --- 結果表示 --- ')
from operator import itemgetter
noun_list.sort(key=itemgetter(1))
noun_list.reverse()
for i, item in enumerate(noun_list):
  if i == 20:
    break
  print(item)