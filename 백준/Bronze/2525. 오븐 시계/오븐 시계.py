A, B = map(int, input().split())
C = int(input())

minute = B + C

A += minute // 60
B = minute % 60

A %= 24

print(A, B)