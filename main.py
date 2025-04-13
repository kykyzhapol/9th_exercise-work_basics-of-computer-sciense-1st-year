'''
#1st
rings = list(map(int, input().split()))
print(2*rings[0]*rings[2]+2*rings[1])

#2nd
import math as m
num = int(input())
while num > 2:
    num = m.sqrt(num)
    print('{:.3f}'.format(num))

#3rd
icecreams = int(input())
div = []
for i in range(2, icecreams+1):
    if icecreams % i == 0:
        div.append(i)
print(div[0])

#4th
k = []
while 0 not in k:
    k.append(int(input()))
countt = 0
for i in k:
    if i%4 == 0:
        countt +=1
print(countt)

#5th
num = range(100000, 1000000)
poll = []
for i in range(0, len(num)-3):
    n1 = list(str(num[i]))
    n2 = list(str(num[i+1]))
    n3 = list(str(num[i+2]))
    n4 = list(str(num[i+3]))
    if n1[1] == n1[5] and n1[2] == n1[4]:
        if n2[1] == n2[5] and n2[2] == n2[4]:
            if n3[1] == n3[4] and n3[2] == n3[3]:
                if n4[0] == n4[5] and n4[1] == n4[4] and n4[2]==n4[3]:
                    poll.append(num[i])
print(poll)
'''



