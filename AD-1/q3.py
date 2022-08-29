"""
Faça um programa, contendo subprograma(s), que leia linhas da entrada padrão até que
uma linha vazia seja digitada. Com exceção da última, todas as outras linhas possuem uma
ou mais palavras. Identifique e escreva:
(a) a linha que possua mais vogais sem acento;
(b) a palavra de maior comprimento, caso haja empate escreva uma delas;
(c) a linha que possua mais palavras palíndromas. Caso haja empate escreva uma delas.
Definição: uma palavra é dita palíndromo se e somente se o primeiro caracter é igual ao
último. Caso exista, o segundo é igual ao penúltimo. E assim sucessivamente. Exemplos:
o, ama, adida e socorrammesubinoonibusemmarrocos.
"""

VOGAIS_SEM_ACENTO = ("a", "e", "i", "o", "u")
VOGAIS_COM_ACENTO = ("á", "é", "í", "ó", "ú", "â", "ê", "ô", "û", "à", "è", "ì", "ò", "ù")

lista_entradas = []

ligado = True

while ligado:
    entrada = input("Digite uma frase:\n")
    if entrada == '':
        ligado = False
    else:
        lista_entradas.append(entrada)

maior_frase = ''

if len(lista_entradas) == 0:
    print("Nenhuma linha não vazia foi lida!!")
else:
    # Pegar linha com mais vogais sem acentos
    for frase in lista_entradas:
        for item in VOGAIS_COM_ACENTO:
            if item in frase.lower():
                print('nop')
            else:
                print(frase)
    # Pegar a palavra com maior comprimento
    # Pegar a linha com mais palavras palindromas
