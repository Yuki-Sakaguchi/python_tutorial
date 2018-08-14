# -*- coding: utf-8 -*-

# 引数を受け取る
import sys
args = sys.argv

# 引数チェック
if len(args) != 2 or not args[1]:
  s = "吾輩は猫である"
  print("引数が不正なためサンプルとして、[ " + s + " ]を使用します")
else:
  s = args[1]
  print("[ " + s + " ]を使用します")

# 形態素解析
from janome.tokenizer import Tokenizer

t = Tokenizer()

# 解析
for token in t.tokenize(s):
  print(token)
  # print(token.surface, '\t')                  # 表層形
  # print(token.part_of_speech.split(',')[0])   # 品詞
  # print(token.part_of_speech.split(',')[1])   # 品詞細分類1
  # print(token.part_of_speech.split(',')[2])   # 品詞細分類2
  # print(token.part_of_speech.split(',')[3])   # 品詞細分類3
  # print(token.infl_type)                      # 活用型
  # print(token.infl_form)                      # 活用形
  # print(token.base_form)                      # 原形
  # print(token.reading)                        # 読み
  # print(token.phonetic)                       # 発音
  # print(token.node_type)                      # node_type
  