# -*- coding: utf-8 -*-

# 引数を受け取る
import sys

# 引数を変数に格納
args = sys.argv

# 引数があるかどうか
if len(args) != 3:
  print("引数が不正なため、処理を終了します")
  sys.exit()

def isInt(num):
  return num and num.isdigit()

for i in range(len(args)):
  if i == 0:
    continue
  if not isInt(args[i]):
    print("数字じゃない引数が混ざっていたので処理を終了します -> " + args[i])
    sys.exit()

# 引数を足す
def add(x, y):
  sum = str(int(x) + int(y))
  print(x + " + " + y + " = " + sum)

add(args[1], args[2])
