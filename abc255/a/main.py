# デバッグ
# oj t -c "python3 main.py" -d tests

# 提出
# acc submit



# 入力：N(文字列または数)========================

#str型で受け取るとき
# s = input()
#int型で受け取るとき
# s = int(input())
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
# R, C = input().split()
# >>>print(A)
# Alice

# 入力：A B(整数)--------------------------
# 例；1 3
# ---------------------------------------

R, C = map(int, input().split())
# >>>print(A)
# 1
# >>>print(A,B)
# 1 3

# 入力：数がN個の場合------------------------
# 例；A1 A2 A3...AN
# ----------------------------------------

#list型で取得
A11, A12 = list(map(int, input().split()))
A21, A22 = list(map(int, input().split()))
# >>>print(l)
# [1, 3, 4, 5, 6]

# 入力：文字列と数字の複合------------------------
# N, S = map(str, input().split())
# --------------------------------------------

# print(R,C)

# hoge = []

# for r in range(2):
  # hoge.append = list(map(int, input().split()))
  # hoge.append = list(map(int, input().split()))
  # A11,A12 = map(int, input().split())
  # A21,A22 = map(int, input().split())
# hoge.append(A11)
# hoge.append(A12)
# hoge.append(A21)
# hoge.append(A22)


#  A11s = A11
#   A12s = A12,
#   A21s - A21,
#   A22s = 22

# print(R, C)

# print("A11:",A11)
# print("A12:",A12)
# print("A21:",A21)
# print("A22:",A22)


# print(R)
# print(C)


if(R==1 and C==1):
  # print("A11")
  print(A11)
elif(R==1 and C==2):
  # print("A12")
  print(A12)

elif(R==2 and C==1):
  # print("A21")
  print(A21)

else:
  # print("A22")
  print(A22)
