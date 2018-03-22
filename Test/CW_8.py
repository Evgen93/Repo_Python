# l = [1, 2, 3, 4, 5, 6, 7]
# for q in range(0, len(l), 2):
#     print(l[q])

#################################
# l = [1, 21, 3, 34, 5, 60, 7]
# for q in l:
#     if q % 2 == 0:
#         print(q)
##################################
# l = [1, 21, 3, 34, 5, 60, 7]
# for q in range(1, len(l)):
#         if l[q] > l[q - 1]:
# #             print(l[q])
# ##################################
# l = [1, 2, -3, 4, -5, 6, 7]
# for q in range(1, len(l)):
#         if l[q] > 0 and  l[q - 1] > 0:
#             print(l[q - 1], l[q])
# #################################
# l = [1, 2, -3, 4, -5, 9, 7]
# count = 0
#
# for q in range(1, len(l) - 1):
#     if l[q - 1] < l[q] > l [q + 1]:
#         count += 1
#
# print(count)
# ############################################
# l = [10, 2, -3, 11, -5, 9, 7]
# max = l[0]
# ind = 0
#
# for q in range(1, len(l)):
#     if max < l[q]:
#         max = l[q]
#         ind = q
#
# print(max)
# print(ind)
# ############################################
# l = [183, 172, 169, 168, 168, 153, 143]
# x = int(input("Введите рост Пети: "))
#
# for q in range(0, len(l)):
#     if x > l[q]:
#         l.append(x)
#         break
#     else:
#         l.insert(len(l), x)
#         break
#
# print(l)
##############################################
# l = [183, 172, 188, 188, 188, 159, 159]
#
# el = len(l)
# for q in range(0, len(l) - 1):
#     for i in range(q + 1, len(l) - 1):
#             if l[q] == l[i]:
#                 l.remove(l[i])
#                 i -= 2
#
# print(l)
##############################################
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# for q in range(0, len(l), 2):
#     if q
#     temp = l[q]
#     l[q] = l[q + 1]
#     l[q + 1] = temp
#
# print(l)
# ############################################
# l = [10, 2, -3, 11, -5, 9, 7]
# max = l[0]
# indMax = 0
# min = l[0]
# indMin = 0
#
# for q in range(1, len(l)):
#     if max < l[q]:
#         max = l[q]
#         indMax = q
#     if min > l[q]:
#         min = l[q]
#         indMin = q
#
# temp = l[indMax]
# l[indMax] = l[indMin]
# l[indMin] = temp
#
# print(l)
#############################################