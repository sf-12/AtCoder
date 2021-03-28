#!/usr/bin/env python3

import math
import string

# 入力
n = int(input())
s = input().split()
# print(n)
# print(s)

# 演算

result = []

# bit全探索
for i in range(2 ** (n-1)):
  print(str(i) + "=========")
  ores = int(s[0])
  xores = 0
  xoresFlag = False

  for j in range(n-1):
    if( (i>>j) & 1):
      xores ^= ores
      ores = 0
      xoresFlag = True
    else:
      ores |= int(s[j+1])
    print( "ores:" + str(ores) + " xores:" + str(xores))

  if xoresFlag == True:
    result.append(xores)
  else:
    result.append(ores)

# 出力
print(result)
print(min(result))
