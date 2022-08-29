"""
Faça um programa uma ou mais linhas. A última linha lida será uma linha vazia. Com
exceção da última, cada uma das demais contém um número de ponto flutuante (float)
cada. Calcule e escreva na saída padrão a soma de todos os números lidos e a média dos
números lidos, ambos com dupla precisão. Caso a primeira linha lida seja vazia escreva na
saída padrão a mensagem: "Nenhuma linha lida com conteúdo, portanto não há soma nem
média!"
"""

lista_entradas = []

ligado = True

while ligado:
    entrada = input("Insira um número:\n")
    if entrada == '':
        ligado = False
    else:
        lista_entradas.append(int(entrada))

soma_entradas = float(sum(lista_entradas))
media_entradas = soma_entradas / len(lista_entradas)

if lista_entradas == []:
    print("Nenhuma linha lida com conteúdo, portanto não há soma nem média!")
else:
    print(f"Soma dos Números: {soma_entradas}")
    print(f"Média dos Números: {media_entradas}")
