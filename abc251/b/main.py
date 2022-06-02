import itertools

# 入力：N(文字列または数)========================

#str型で受け取るとき
# s = input()
#int型で受け取るとき
# s = int(input())
#float型　(小数)で受け取るとき
# s = float(input())

# (1,N)行列データ==============================

# 入力：A B(文字列)------------------------
# 例；Alice Bob Charlie

#list型で受け取るとき
# s = input().split()
# >>>print(s)
# ['Alice', 'Bob', 'Charlie']

#文字列として受け取るとき
# A, B, C = input().split()
# >>>print(A)
# Alice

# 入力：A B(整数)------------------------
# 例；1 3

A, B = map(int, input().split())
# >>>print(A)
# 1
# >>>print(A,B)
# 1 3

# 入力：数がN個の場合------------------------
# 例；A1 A2 A3...AN

#list型で取得
l = list(map(int, input().split()))
# >>>print(l)
# [1, 3, 4, 5, 6]

# 入力：文字列と数字の複合------------------------
# N, S = map(str, input().split())

# (N,1)行列データ==============================


# print(A)
# print(B)
# print(l)


good_list = []

l_len = len(l)


list1 = list(itertools.combinations(l, 1))
list2 = list(itertools.combinations(l, 2))
list3 = list(itertools.combinations(l, 3))

list_all = list1 + list2 + list3


# print(list_all)


new_list = []
for el in list_all:
  sumel = sum(el)
  if(sumel <= B):
    new_list.append(sumel)


print(len(set(new_list)))