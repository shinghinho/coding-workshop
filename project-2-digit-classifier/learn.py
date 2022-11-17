def error(y, z):
    n = len(y)
    s = 0
    for i in range(n):
        s += abs(y[i] - z[i])
    return s/n

x = [[2, 4], [-2, 3], [3, -1], [5, -2]]
y = [17, 5, 3, 4]

def predict(m, x):
    return m[0] * x[0] + m[1] * x[1]

def learn(x, y, z, m):
    return m + (y - z) * 0.01 * x

def test(m):
    z = []
    for i in range(len(y)):
        z.append(predict(m, x[i]))
    print(error(y, z))

m = [10, 20]
test(m)

for a_variable in range(1000):
    for i in range(len(y)):
        xi = x[i]
        yi = y[i]
        z = predict(m, x[i])
        m[0] = learn(x[i][0], y[i], z, m[0])
        m[1] = learn(x[i][1], y[i], z, m[1])

test(m)
print(m)

