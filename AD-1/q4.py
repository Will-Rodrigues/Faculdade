"""
Faça um programa, contendo subprograma(s), que, recursivamente, calcule a potência de
um número inteiro na base b elevado ao expoente inteiro exp. Para tal, faça as seguintes
etapas:
(a) Receba dois valores de entrada;
(b) Utilizando subprograma, verifique se os elementos são inteiros. Se alguma das entradas
não for do tipo inteiro então retorne dizendo especificamente qual entrada não foi inteira.
Se ambas as entradas não forem do tipo inteiro, então retorne dizendo que ambas as
entradas não são do formato correto.
(c) Se ambos os elementos da entrada forem do tipo inteiro, utilizando chamadas
recursivas, obtenha o valor b^exp.
"""

entrada_1 = input("Digite a base:\n")
entrada_2 = input("Digite o expoente:\n")

if entrada_1.isdigit() and entrada_2.isdigit() == False:
    print(f"Expoente {entrada_2} não está no formato devido")
elif entrada_2.isdigit() and entrada_1.isdigit() == False:
    print(f"Base {entrada_1} não está no formato devido")
elif entrada_2.isdigit() == False and entrada_1.isdigit() == False:
    print(f"Base {entrada_1} e expoente {entrada_2} não estão no formato devido")
else:
    print(f"{entrada_1} elevado a {entrada_2} é igual a {int(entrada_1) ** int(entrada_2)}")
