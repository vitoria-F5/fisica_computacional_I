'''
def vT(r,T):
    c = 2 * 3.14 * r
    return c / T

def pa(primeiro, razao, lugar):
    #soma = 0 
    for i in range(lugar):  # corrigido: usar 'lugar' como quantidade de termos
        termo = primeiro + i * razao
        print(termo)
        #soma = soma + termo  # soma correta dos termos
    return termo    

loop = input("Vamos jogar? Responda específicamente com Sim ou Não.")
if (loop == "Sim"):
    condicao = True
    
    while(condicao):
        quantidade = int(input("Quantos números você quer nessa progressão?"))
        primeiro = int(input("Digite o primeiro número:"))
        razao = int(input("Digite a razão da progressão aritmética:"))
        lugar = int(input("Digite a posição que você quer parar:"))
        an = primeiro + (lugar-1)*razao
        
        print(f"O número na posição {lugar} é {an}", pa(primeiro, razao, lugar))
        print("") #linha vazia

else:
    print("Você é realmente muito chato(a)!")
'''

def pa(primeiro, razao, quantidade):
    for i in range(quantidade):
        termo = primeiro + i * razao
        print(termo)
    return termo  # retorna o último termo

loop = input("Vamos jogar? Responda específicamente com Sim ou Não.")
if (loop == "Sim"):
    condicao = True

    while(condicao):
        quantidade = int(input("Quantos números você quer nessa progressão?"))  # quantidade de termos
        primeiro = int(input("Digite o primeiro número:"))
        razao = int(input("Digite a razão da progressão aritmética:"))

        print("Os termos da progressão são:")
        pa(primeiro, razao, quantidade)
        print("Progressão aritmética: a partir do 1° termo, a razão r é somada ao 1° termo para gerar o 2° termo, " \
        "logo, de um termo para o outro,a diferença sempre é igual à razão.")
        
        print("Progressão geométrica: a partir do 1° termo, a razão q é multiplicada pelo 1° termo para gerar o 2° termo, " \
        "logo, a divisão do termo pelo seu antecessor sempre é igual à razão.")
else:
    print("Você é realmente muito chato(a)!")