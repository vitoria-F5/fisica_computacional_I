# Calculando Bhaskara

print("y = a * x² + b * x + c")

a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
c = int(input("Digite um número: "))

print("y =", a, "* x² +", b,"* +", c)

delta = b**2 - 4 * a * c

if(delta <0):
    print("A equação não tem raiz real")
else:
    x1 = (-b + (delta**(1/2)))/2*a 
    x2 = (-b - (delta**(1/2)))/2*a
    print("As raízes são:", x1, "e", x2)


print("Você gostaria de saber se os números são primos? Digite com S para sim ou N para não.")
resposta = input()

print ("Um número é classificado como primo se ele é maior do que um e é divisível apenas por um e por ele mesmo")

# Função que verifica se um número é primo
def primos(n):
    # 0 e 1 não são primos por definição
    if n <= 1:
        return False

    # Verifica se n é divisível por algum número entre 2 e (n-1). 
    # Se testássemos até n, o número n sempre seria divisível por ele mesmo. Todo número é divisível por si mesmo.
    for i in range(2, n-1):
        if n % i == 0:
            return False

    # Se não for divisível por nenhum número, é primo
    return True

# Verifica se o usuário quer saber se os números são primos
if resposta == "S":
    print("Os números:", a, b, c, "que você inseriu são respectivamente:")
    
    for numero in [a, b, c]:
        if primos(numero):
            print(numero, "é primo")
        else:
            print(numero, "não é primo")
else:
    print("Você é realmente muito chato...")





 
