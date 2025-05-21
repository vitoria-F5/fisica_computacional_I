def vT(r,T):
    c = 2 * 3.14 * r
    return c / T

# Função de Somatório
def somatorio(inicio, fim):
    soma = 0 
    for i in range(inicio,fim+1):
        soma = soma + i
    return soma

loop = input("Qual loop: ")
if (loop == "while"):
    condicao = True
    while(condicao):
        r = float(input("Digite o raio:"))
        T = float(input("Digite o período:"))
        aC = vT(r,T)**2 / r
        print(f"A aceleração centrípeta para r = {r} e período = {T} é", aC)
        print("") #linha vazia

        resposta = input("Você deseja calcular outra aceleração centrípeta? (s/n)")
        if(resposta == "n"):
            condicao = False
    print("Você saiu do loop")
    print("")

else:
    inicio = int(input("Digite o primeiro número:"))
    fim = int(input("Digite o último número:"))
    print(f"A soma final é de {inicio} até {fim} é", somatorio(inicio, fim))
