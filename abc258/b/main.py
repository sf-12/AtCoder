# デバッグ
# oj t -c "python3 main.py" -d tests

# 提出
# acc submit



# 入力：N(文字列または数)========================

#str型で受け取るとき
# s = input()
#int型で受け取るとき
N = int(input())
#float型(小数)で受け取るとき
# s = float(input())

# (1,N)行列データ==============================

# 入力：A B(文字列)------------------------
# 例；Alice Bob Charlie
# ---------------------------------------

#list型で受け取るとき
# s = input().split()
# >>>print(s)
# ['Alice', 'Bob', 'Charlie']

#文字列として受け取るとき
# A, B, C = input().split()
# >>>print(A)
# Alice

# 入力：A B(整数)--------------------------
# 例；1 3
# ---------------------------------------

# A, B = map(int, input().split())
# >>>print(A)
# 1
# >>>print(A,B)
# 1 3

# 入力：数がN個の場合------------------------
# 例；A1 A2 A3...AN
# ----------------------------------------

#list型で取得
# l = list(map(int, input().split()))
# >>>print(l)
# [1, 3, 4, 5, 6]

# 入力：文字列と数字の複合------------------------
# N, S = map(str, input().split())
# --------------------------------------------

A= []

# if N == 1:
#  return A[0]


for n in range(N):
  # l = list(map(int, input().split()))
  l = list(map(str, input().split()))
  A.append(l)

# l.add(all)

# print(N)
# print(A)

maxInt = 0

nowRow = 0
nowCol = 0
nowNum = 0

# 0 上
# 1　右上
# 2　右
# 3　右下
# 4　下
# 5　左下
# 6　左
# 7　左上

for dim in range(8):
# for aaa in range(1):
  # dim = 7
  # print("dim:",dim)
  for row in range(N):
    # print(" row:",row)
    nowRow = row
    for col in range(N):
      # print(" col:",col)
      nowCol = col
      tempInt = 0
      for step in range (N):
        # print("  step:",step)
        # print("   nowRow:",nowRow)
        # print("   nowCol:",nowCol)
        # print("   A[nowRow]:",A[nowRow][0])
        # print("   A[nowRow][nowCol]:",int(A[nowRow][0][nowCol]))

        tempInt = tempInt * 10 + int(A[nowRow][0][nowCol])
        # print("tempInt:", tempInt)

        if dim == 0:
          # 上
          nowRow = nowRow - 1
          if nowRow < 0:
            nowRow = N - 1
        elif dim == 1:
          # 右上
          nowRow = nowRow - 1
          if nowRow < 0:
            nowRow = N - 1
          nowCol = nowCol + 1
          if nowCol > N - 1:
            nowCol = 0
        elif dim == 2:
          # 右
          nowCol = nowCol + 1
          if nowCol > N - 1:
            nowCol = 0
        elif dim == 3:
          # 右下
          nowRow = nowRow + 1
          if nowRow > N - 1:
            nowRow = 0
          nowCol = nowCol + 1
          if nowCol > N - 1:
            nowCol = 0
        elif dim == 4:
          # 下
          nowRow = nowRow + 1
          if nowRow > N - 1:
            nowRow = 0
        elif dim == 5:
          # 左下
          nowRow = nowRow + 1
          if nowRow > N - 1:
            nowRow = 0
          nowCol = nowCol - 1
          if nowCol < 0:
            nowCol = N - 1
        elif dim == 6:
          # 左
          nowCol = nowCol - 1
          if nowCol < 0:
            nowCol = N - 1
        elif dim == 7:
          # 左上
          nowRow = nowRow - 1
          if nowRow < 0:
            nowRow = N - 1
          nowCol = nowCol - 1
          if nowCol < 0:
            nowCol = N - 1

      if tempInt > maxInt:
        maxInt = tempInt

print(maxInt)