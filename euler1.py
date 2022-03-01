total = []

for n in range (0, 1000):
    if (n % 3 == 0) or (n % 5 == 0):
        total.append(n)


resultado = sum(total)
print(resultado)
