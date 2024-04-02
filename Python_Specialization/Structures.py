x = ["Mickael Jackson", 10.1, 1982, [1, 2], ("A", 1)]
x.extend(["pop", 10])
x.append(["pip", 20])
x[0] = "Joseph Miazza"
del (x[0])
x.insert(0, "Mickael Jackson")
L = x[0].split(" ")
del (x[0])
x.insert(0, L)
print(x)
print(type(x))
B = x[:]
print(B)
del (x[3])
print(x)
print(B)