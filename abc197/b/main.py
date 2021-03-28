#!/usr/bin/env python3

import math
import string

# 入力
numbers = input().split()
rowNum =int(numbers[0])
colNum =int(numbers[1])
rowPos =int(numbers[2]) - 1
colPos =int(numbers[3]) - 1
S = [ input() for i in range(rowNum)]

# 演算
counter = 1

i = 1
while True:
  if rowPos - i >= 0 and S[rowPos - i][colPos] == ".":
    counter += 1
    # print("U")
    i = i + 1
  else:
    break

j = 1
while True:
  if rowPos + j < rowNum and S[rowPos + j][colPos] == ".":
    counter += 1
    # print("D")
    j = j + 1
  else:
    break

k = 1
while True:
  if colPos - k >= 0 and S[rowPos][colPos - k] == ".":
    counter += 1
    # print("L")
    k = k + 1
  else:
    break

l = 1
while True:
  if colPos + l < colNum and S[rowPos][colPos + l] == ".":
    counter += 1
    # print("R")
    l = l + 1
  else:
    break

# 出力
print(counter)
