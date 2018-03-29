# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fact(n - 1)
#
# print(fact(5))
#
# l = [1, 2, 3, 4, 5]
#
#
# def f1_sum(l):
#     res = 0
#     for q in l:
#         res += q
#     return res
#
#
# def f2_sum(l, size):
#     if size == -1:
#         return 0
#     else:
#         return l[size] + f2_sum(l, size - 1)
#
#
# print(f1_sum(l))
# print(f2_sum(l, len(l) - 1))

l = [[1, 2, [3, [4, 5]], 6, 7, [8, [9]]]]
ll = [1, [2, 3], 4]
_len = len(l) - 1


def f3(l):
    s = str(l)
    l1 = []
    for q in s:
        if q == "," or q == ' ' or q == '[' or q == ']':
            continue
        else:
            l1.append(int(q))

    return l1


def f1(ll):
    l1 = []

    for q in ll:
        l1.append(q)

    return l1
