# h, w, l = [int(a) for a in input().strip().split()]
# ground = [[] for _ in range(h)]
#
# for i in range(h):
#     ground[i] = [int(a) for a in input().strip().split()]
#
# def flow(i, j):
#     if ground[i][j] > l or ground[i][j] == -1:
#         return
#     ground[i][j] = -1
#     if i > 0:
#         flow(i-1, j)
#     if i < h-1:
#         flow(i+1, j)
#     if j > 0:
#         flow(i, j-1)
#     if j < w-1:
#         flow(i, j+1)
#     return
#
# for x in range(w):
#     flow(0, x)
#     flow(h-1, x)
#
# for x in range(1, h-1):
#     flow(x, 0)
#     flow(x, w-1)
#
# sum = 0
# for i in range(h):
#     for j in range(w):
#         if ground[i][j] != -1:
#             sum += 1
#
# print(sum)
a = [1,2]
print(a)