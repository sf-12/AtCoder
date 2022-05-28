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
H, W = input().split()
H = int(H)
W = int(W)
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
# HW = []
# for():
#   h = list(map(str, input().split()))
#   W = 

# >>>print(l)
# [1, 3, 4, 5, 6]

# 入力：文字列と数字の複合------------------------
# N, S = map(str, input().split())
# --------------------------------------------


# N = int(input())
# xy = [input().split() for _ in range(H)]
# x, y = [list(i) for i in zip(*xy)]

# print(l)

l = []

for h in range(H):
  x = list(input().split())
  l.append(x)



# print(H)
# print(W)

# print(l)
# print(l[0])

# chars = list("".join(l[0]))
# print(chars)

# print(type(l[0]))
# print(list(l[0]))

# print(list(l[0]))

pos1 = []
pos1flg = False
pos2 = []

for h in range(H):
  for w in range(W):
    moji = list("".join(l[h]))[w]
    # print(moji)
    if(moji == "o"):
      if pos1flg == True:
    # if((l[h][w] == "o") & pos1flg == True):
        # print("pos2 OK")
        pos2 = [h, w]
      else:
        # print("pos1 OK")
        pos1 = [h, w]
        pos1flg = True

# print(pos1)
# print(pos2)

ans = abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
print(ans)