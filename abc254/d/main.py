# デバッグ
# oj t -c "python3 main.py" -d tests

# 提出
# acc submit
import itertools


# 入力：N(文字列または数)========================

#str型で受け取るとき
# s = input()
#int型で受け取るとき
s = int(input())
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



def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

# print(s)

li = list(range(s))

kumi = list(itertools.combinations(li, 2))

# print(kumi)

# print(li)

# print(prime_factorize(s))

nu = 0

for ku in kumi:
  kake = ku[0] * ku[1]
  # print(kake)
  # 
  aa = prime_factorize(kake)
  aaset = set(aa)
 
 
  if(len(aa) == len(aaset) *2 ):
    nu = nu +1

print(nu)