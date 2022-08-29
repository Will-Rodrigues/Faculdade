"""
Faça um programa, contendo subprograma(s), que, receba duas strings na entrada, não
necessariamente com os mesmos tamanhos, e identificado qual a string de menor tamanho
dentre as duas, retorne uma subcadeia da maior string que esteja com o menor número de
caracteres diferentes comparada com a menor string. Retorne o número de caracteres
distintos, qual a posição que se inicia essa subcadeia com menor número de caracteres
distintos e também a string de maior tamanho. Faça tal como os testes abaixo.
"""
string1 = input("Digite o primeiro texto:\n")
string2 = input("Digite o segundo texto:\n")

# ----- Identificando qual a maior string

len_string1 = len(string1)
len_string2 = len(string2)

if len_string1 > len_string2:
    maior_string = string1
    menor_string = string2
else:
    maior_string = string2
    menor_string = string1

# ----- Descobrindo a maior substring possível entre as duas strings

res = [maior_string[i: j] for i in range(len(maior_string)) for j in range(i + 1, len(maior_string) + 1)]

res2 = [menor_string[i: j] for i in range(len(menor_string)) for j in range(i + 1, len(menor_string) + 1)]

maior_substring = ''

for i in res:
    for j in res2:
        if i == j:
            if len(j) > len(maior_substring):
                maior_substring = j

# ----- Descobrindo a diferença de caracteres da substring para a menor string

dif_caracteres = len(menor_string) - len(maior_substring)

# ----- Descobrindo a posição que a substring tem na string
posicao = maior_string.find(maior_substring) + 1

print(f"A subcadeia mais próxima tem {dif_caracteres} caracteres distintos e começa na posição {posicao} da cadeia {maior_string}")