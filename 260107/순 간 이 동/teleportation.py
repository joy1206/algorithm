a, b, x, y = map(int, input().split())

# A -> B
dist1 = abs(a-b)

# A -> X -> Y -> B
dist2 = abs(a-x) + abs(y-b)

# A -> Y -> X -> B
dist3 = abs(a-y) + abs(x-b)

print(min(dist1, dist2, dist3))