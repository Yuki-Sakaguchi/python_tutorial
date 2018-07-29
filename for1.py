# -*- coding: utf-8 -*-

# 文字列でくりかえし
for char in "HELLO":
  print(char)

print(" --- ")

# 数字で繰り返し（0始まり）
for i in range(5):
  print(i)

print(" --- ")

# 数字で始まりの値を指定する
for i in range(2, 7):
  print(i)

print(" --- ")

# 配列のループ
str_list = ['ruby', 'python', 'perl', 'java', 'c']
for string in str_list:
  print(string)

print(" --- ")

# continue
num_list = [100, 80, 70, 60, 50]
for num in num_list:
  if num >= 80:
    continue
  print(num)

print(" --- ")

# breakとfor-else
num_list = [100, 80, 70, 60, 50]
for num in num_list:
  if num <= 40:
    print(num)
    break
else:
  # ループ完了後にbreakしなければfor-elseに入る
  print('一致するものがありませんでした')

print(" --- ")

