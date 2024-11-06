import sys

def progress(x, y, n):
  step = 0
  while x <= n and y <= n:
    if x < y:
      x += y
    else:
      y += x
    step += 1
  return step

input = sys.stdin.readline
num = int(input())

for _ in range(num):
  A, B, N = map(int, input().strip().split())
  result = progress(A, B, N)
  print(result)