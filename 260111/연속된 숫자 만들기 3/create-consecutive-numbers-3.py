a = list(map(int, input().split()))
a.sort()

gap1 = a[1] - a[0] -1
gap2 = a[2] - a[1] -1
print(max(gap1, gap2))