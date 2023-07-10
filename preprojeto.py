nome = "João"
idade = 45
peso = 85.3
ehBrasileiro = True

print("nome:" + str(type(nome)))
print("idade:" + str(type(idade)))
print("peso:" + str(type(peso)))
print("ehBrasileiro:" + str(type(ehBrasileiro)))

print(nome)
print(idade)
print(peso)
print(ehBrasileiro)

# Operações com strings
comp = "João" > "Pedro"
print(comp)

comp = "João" == "Pedro"
print(comp)

sub = "Jose" in "Josevaldo"
print(sub)

parts = "idade,peso,altura".split(",")
print(parts)

# Operadores lógicos
comp = 4 < 5 and 9 > 10
print(comp)
comp = 4 < 5 or 9 > 10
print(comp)
comp = 4 < 5 and not (9 > 10)
print(comp)

# commando print
x = 3
y = 4
print(x, "elevado a", y, "é", x**y)
print(str(x) + " elevado a " + str(y) + " é " + str(x**y))