def CountWord(f):
    l = 0
    with open(f) as f:
        for line in f:
           l += len(line.split())

    return l

def FindLongWord(f):
    l = []
    with open(f) as f:
        for line in f:
            l.append(line.split())
        res = l[0][0]
        for q in l:
            for i in q:
                if len(res) < len(i):
                    res = i
    return res

def Del(s = "qwerty"):
    s = list(s)
    i = 0
    while i < len(s) - 1:
        if s[i] == "'" or s[i] == '"' or s[i] == "." or s[i] == "," or s[i] == "!" or s[i] == "?" or s[i] == ":" or s[i] == ";":
            s.remove(s[i])
            i -= 2
        i += 1


    return s
# def FindRepWord(f):
#     l = []
#     with open(f) as f:
#         for line in f:
#             l.append(line.split())
#
#         for q in l:
#             for i in q:
