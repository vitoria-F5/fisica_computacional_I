x = 20
y = 8

print("x = " + str(x) + " e y = " + str(y))
print(" ")

# adição
print(str(x) + " + " + str(y) + " = " + str(x+y) + " soma")
print(" ")

# multiplicação
print(str(x) + " * " + str(y) + " = " + str(x*y) + " multiplicação")
print(" ")

# subtração
print(str(x) + " - " + str(y) + " = " + str(x-y) +" subtração")
print(" ")

# divisão
print(str(x) + " / " + str(y) + " = " + str(x/y) + " divisão")
print(" ")

# divisão inteira
print(str(x) + " // " + str(y) + " = " + str(x//y) + " divisão inteira")
print(" ")

# resto da divisão
print(str(x) + " % " + str(y) + " = " + str(x%y) + " resto da divisão")
print(" ")

# exponencial
print(str(x) + "^" + str(y) + " = " + str(x ** y) + " exponencial")
print(" ")

# igual
print(str(x) + " = " + str(y) + " => " + str(x == y))
print(str(x) + " = " + str(x) + " => " + str(x == x))
print(" ")

# diferente
print(str(x) + " ≠ " + str(y) + " => " + str(x != y))
print(str(x) + " ≠ " + str(x) + " => " + str(x != x))
print(" ")

# ou
print(str(x) + " = 20 ou " + str(y) + " = 10 => " + str(x == 20 or y == 10))
print(str(x) + " = 10 ou " + str(y) + " = 8 => " + str(x == 10 or y == 8))
print(str(x) + " = 20 ou " + str(y) + " = 8 => " + str(x == 20 or y == 8))
print(str(x) + " = 4 ou " + str(y) + " = 6 => " + str(x == 4 or y == 6))
print(" ")

# ou exclusivo
print(str(x) + " = 3 ou exclusivo " + str(y) + " = 8 => " + str((x == 3) ^ (y == 8)))
print(str(x) + " = 20 ou exclusivo " + str(y) + " = 3 => " + str((x == 20) ^ (y == 3)))
print(str(x) + " = 20 ou exclusivo " + str(y) + " = 8 => " + str((x == 20) ^ (y == 8)))
print(" ")

# # e
print(str(x) + " = 20 e " + str(y) + " = 8 => " + str((x == 20) & (y == 8)))
print(str(x) + " = 20 e " + str(y) + " = 3 => " + str((x == 20) & (y == 3)))
print(str(x) + " = 3 e " + str(y) + " = 8 => " + str((x == 3) & (y == 8)))
print(" ")

# maior
print(str(x) + " > " + str(y) + " = " + str(x > y))
print(str(y) + " > " + str(x) + " = " + str(y > x))
print(" ")

# menor
print(str(x) + " < " + str(y) + " = " + str(x < y))
print(str(y) + " < " + str(x) + " = " + str(y < x))
print(" ") 

# verificar se o número é ímpar
print(str(x) + " é ímpar => " + str(x % 2 != 0))
print(str(y) + " é ímpar => " + str(y % 2 != 0))
print(" ")

# verificar se o número é par
print(str(x) + " é par => " + str(x % 2 == 0))
print(str(y) + " é par => " + str(y % 2 == 0))
print(" ")

