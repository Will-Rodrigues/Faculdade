'''
Faça um programa, contendo subprograma(s), que leia inicialmente a quantidade de linhas
que serão digitadas em seguida contendo um ou mais números inteiros por linha.
Identifique e escreva na saída padrão o menor e o maior de todos os números lidos.
'''

lista_entradas = []

linhas = int(input("Quantas linhas serão digitadas?\n"))

if linhas > 0:

    for n in range(linhas):
        entrada = input("Insira os números:\n")
        numeros = entrada.split(" ")
        for numero in numeros:
            lista_entradas.append(int(numero))

    maior_numero = max(lista_entradas)
    menor_numero = min(lista_entradas)

    print(f"Menor número: {menor_numero} e Maior número: {maior_numero}")

else:
    print("Nenhum número foi lido, portanto, sem mínimo e máximo!!")