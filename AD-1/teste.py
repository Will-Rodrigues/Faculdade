string = 'fundamentosdeprogramacao'
substring = 'dfprof'

# TROCAR O NOME DAS VARIÁVEIS

res = [string[i: j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)]
res2 = [substring[i: j] for i in range(len(substring)) for j in range(i + 1, len(substring) + 1)]

maior_substring = ''

for i in res:
    for j in res2:
        if i == j:
            if len(j) > len(maior_substring):
                maior_substring = j

print(maior_substring)

