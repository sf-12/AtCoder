# デバッグ
# oj t -c "python3 main.py" -d tests

# 提出
# acc submit


X, A, D ,N = map(int, input().split())

An = []


for n in range(N):
  # print(n)
  An.append(A + (n-1)*D)

print(An)

