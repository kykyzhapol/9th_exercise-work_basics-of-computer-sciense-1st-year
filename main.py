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

#6th
ans = []
for i in range(10, 100):
    if (str(i) in str(i**2)) and (i**2<1000) and ((i**2)%100 == i):
        ans.append(i**2)
print(ans)

#7th
import tqdm
ans = []
for i in tqdm.tqdm(range(1000, 10000)):
    n1 = list(str(i))
    for k in range(1000, 10000):
        n2 = list(str(k))
        n3 = list(str(i+k))
        if n3[3] == n2[3] == n1[1] and n3[2] == n1[2] and n3[1] == n2[1] and n3[0] == n2[0] and (n3[4] not in n2 and n1)\
                and (n2[2] not in n1 and n3) and (n1[0] and n1[3] not in n2 and n3):
            ans.append([i, k, i+k])
print(ans)

#8th
import math as m
num = int(input())
qrts = 0
for i in range(num+1):
    for k in range(num+1):
        if i**2 + k**2 == num:
            qrts+=1
print(qrts//2)

#9th
import math as m
n = int(input())
print(m.factorial(n+2)/((n+2)/2))

#10th
import math as m
q = int(input())

def inverse_factorial(n):
    k = 1
    factorial = 1

    while factorial < n:
        k += 1
        factorial *= k

    return k if factorial == n else None

q_st = inverse_factorial(q)-1
st = []
q_help = inverse_factorial(q)
for i in range(q_st):
    st.append(q_help)
    q_help-=1
q_add = 0

while q_st > 2:
    st[0] += st[q_st]
    st[q_st] = 0
    q_st -= 1
    q_add +=1


print(inverse_factorial(q)+q_add)