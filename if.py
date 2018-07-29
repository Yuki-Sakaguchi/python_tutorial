# -*- coding: utf-8 -*-

# 引数を受け取る
import sys

# 引数を変数に格納
args = sys.argv

# 引数があるかどうか
if len(args) != 2 or not args[1] or not args[1].isdigit():
  print("引数が存在しないか、数字ではないため処理を終了します")
  sys.exit()
else:
  print(args)
  print(args[1])

# 引数の値を調べる
num = int(args[1])
if num > 20:
  print("引数は20より大きいです")
elif num < 10:
  print("引数は10より小さいです")
else:
  print("引数は20以下で10以上です")


