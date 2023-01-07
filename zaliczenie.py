V = 4
M = 2
a = [0.4, 1]
t = [1, 2]



def calc_x(V, M, a, t):
    x = [1] * (V + 1)
    for n in range(1, V + 1):
        sum = 0
        for i in range(0, M):
            if n >= t[i]:
                sum += a[i] * t[i] * x[n - t[i]]
        x[n] = sum / n

    i = 0
    for item in x:
        print('x['+ str(i) +'] = ' + str(item))
        i += 1
    return x



def calc_p0(x):
    sum = 0
    for item in x:
        sum += item
    return 1 / sum



def calc_pn(x, V, M, a, t):
    p = [1] * (V + 1)
    p[0] = calc_p0(x)
    for n in range(1, V + 1):
        sum = 0
        for i in range(0, M):
            if n >= t[i]:
                sum += a[i] * t[i] * p[n - t[i]]
        p[n] = sum / n

    i = 0
    for item in p:
        print('p[' + str(i) + '] = ' + str(item))
        i += 1
    return p



def calc_b(V, P, t, i=1):
    sum = 0
    for n in range(V - t[i - 1] + 1, V + 1):
        sum += P[n]
    return sum



print('M = ' + str(M))
print('V = ' + str(V))
print('a = ' + str(a))

x = calc_x(V, M, a, t)
calc_p0(x)
P = calc_pn(x, V, M, a, t)

i = 1
while i <= M:
    print('b['+ str(i) +'] = ' + str(calc_b(V, P, t, i)))
    i += 1