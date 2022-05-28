
# 試験
# Q = int(input())
# S = []

# for q in range(Q):

#   l = list(map(int, input().split()))
#   l0 = l[0]

#   if l0 == 1:
#     S.append(l[1])

#   elif l0 == 2:
#     l1 = l[1]
#     Snum = S.count(l[2])
#     minNum = min(l[2],Snum)
#     for cnt in range(Snum):
#       if l1 in S:
#         S.remove(l1)
#       else:
#         break

#   else:
#     print(max(S) - min(S))

# 復習
Q = int(input())
S = []

for q in range(Q):

  l = list(map(int, input().split()))
  l0 = l[0]

  if l0 == 1:
    S.append(l[1])

  elif l0 == 2:
    l1 = l[1]
    l2 = l[2]
    Snum = S.count(l1)
    # print(S.find(l1))

    mins = min(l2, Snum)

    while mins > 0:
      S.remove(l1)
      mins -= 1

  else:
    print(max(S) - min(S))

  # print("S:",S)
