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