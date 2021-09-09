# x = [1,2,3,3,2,3,4,3,2,4,4,4]
#
# y = {}
# for i in range(len(x)):
#     if x[i] not in y:
#         y[x[i]] = 1
#     else:
#         y[x[i]]+=1
# mode = 0
# j =list(y.values())
# print(j)
#
# for i in range(len(j)):
#     if mode < j[i]:
#         mode = j[i]
# print(mode)
# for l,m in y.items():
#     if mode ==m:
#         print(l)
#     else:
#         continue
#  k = (y+1)/2
#
# x = [1,2,3,2,3,4,5,5,4,22]
#
# x.sort()
# print(x)
# y = len(x)
# if y%2 == 0:
#     j = int(y/2)
#     print(j)
#     k = int((y/2)+1)
#     print(k)
#     l = (x[j-1]+x[k-1])/2
#     print(l)
# else:
#     k = int((y + 1) / 2)
#     print(x[k-1])

x = [1,2,3,4,5,4,4,4,3,2,2,2,2,2]
y = {}
for i in range(len(x)):
    if x[i] not in y:
        y[x[i]] = 1
    else:
        y[x[i]]+=1
print(y)
mode = 0
j =list(y.values())

print(j)
for i in j:
     if mode < i    :
        mode = i
print(mode)

for k,l in y.items():
    if mode == l :
        print(k)
