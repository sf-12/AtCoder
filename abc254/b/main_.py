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

# print(N)

ans = []

for i in range(N):
  # print(n)
  len_of_Ai = i+1

  An = []

  for j in range(len_of_Ai):

    if(j==0 or j == i):
      aij = 1
    else:
      aij = ans[i-1][j-1] + ans[i-1][j]

    An.append(aij)

  ans.append(An)
  print(" ".join([str(_) for _ in An]))
  # print(" ".join(ans))

# print(ans)
