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
# A, B, C = input().split()
# >>>print(A)
# Alice

# 入力：A B(整数)--------------------------
# 例；1 3
# ---------------------------------------

N, K = map(int, input().split())
# >>>print(A)
# 1
# >>>print(A,B)
# 1 3

# 入力：数がN個の場合------------------------
# 例；A1 A2 A3...AN
# ----------------------------------------

#list型で取得
A = list(map(int, input().split()))
# >>>print(l)
# [1, 3, 4, 5, 6]

# 入力：文字列と数字の複合------------------------
# N, S = map(str, input().split())
# --------------------------------------------

# print("N:",N)
# print("K:",K)
# print("A:",A)

# K=1の時、Yes
if(K==1):
  print("Yes")

else:
  # 昇順かチェック
    # 昇順ならYes
    # そうでなければ以下の処理を行う


  firstflg = True

  for p in range(len(A)-1):
    # print(i)
    if(A[p] > A[p+1]):
      firstflg = False
      break

  # print(firstflg)

  if(firstflg==True):
    print("Yes")
  else:
    nk = N - K
    # print("N - K :", nk)

    changed = True
    while(changed == True):

      changed = False

      # 入れ替え可能ペアについて、ai > aik の時のみ入れ替え
      for i in range(nk):
        # print("i:",i)
        Ai = A[i]
        Aik = A[i+K]
        # print("Ai:",Ai)
        # print("Aik:",Aik)
        if(Ai > Aik):
          A[i] = Aik
          A[i+K] = Ai
          changed = True

    # 入れ替え後が昇順かチェック
      # 昇順であればYes
      # 昇順でなければNo

    flag = True

    for j in range(len(A)-1):
      # print(i)
      if(A[j] > A[j+1]):
        flag = False
        break

    if(flag==True):
      print("Yes")
    else:
      print("No")