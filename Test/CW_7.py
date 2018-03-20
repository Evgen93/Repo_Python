# a = "0123456789"
# print(a[3])
# print(a[len(a) - 1])
# print(a[:len(a) - 2])
# print(a[::2])
# print(a[1::2])
# print(a[::-1])
# print(a[len(a) - 1::-2])
# print(len(a))
#################################
# strk = "Hello python"
# a = strk.count(' ')
#
# print(a)
#################################
# strk1 = "Hello python"
# list1 = strk1.split(' ')
#
# temp = list1[0]
# list1[0] = list1[1]
# list1[1] = temp
#
# strk2 = ' '.join(list1)
# print(strk2)
# #################################
# strk1 = "Hello python"
# ind = int(len(strk1) / 2)
# s = strk1[ind]
# list1 = strk1.split(strk1[ind])
#
# temp = list1[0]
# list1[0] = list1[1]
# list1[1] = temp
# list1[0] = s + list1[0]
#
# strk2 = ' '.join(list1)
# print(strk2)
# #################################
strk1 = "Hello python"
strk2 = "Hellof python"
strk3 = "fHellof fpythonf"

if strk3.count('f') == 1:
    print(strk3.find('f'))
elif strk3.count('f') > 1:
    print(strk3.find('f'))
    print(strk3.split('f'))
else:
    print("Empty")