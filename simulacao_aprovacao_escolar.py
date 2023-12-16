# Simulação de um sistema escolar de aprovação.

def notas(array1, tri):
    i = 1
    while True:
        valor = input(f'Digite a {i}° nota do {tri}° trimestre: ')
        valor = float(valor)
        if valor >= 0 and valor <= 10:
            array1.append(valor)
            i += 1
        elif valor > 10:
            print('Use o programa corretamente!!!')
            continue
        else:
            break
    return

from time import sleep as sl
import numpy as np 

nota = []
notas(nota, 1)
notas_primeiro_trimestre = np.array(nota)
nota = []
notas(nota, 2)
notas_segundo_trimestre = np.array(nota)
nota = []
notas(nota, 3)
notas_terceiro_trimestre = np.array(nota)

# Medias
media_primeiro_trimestre = np.mean(notas_primeiro_trimestre)
media_segundo_trimestre = np.mean(notas_segundo_trimestre)
media_terceiro_trimestre = np.mean(notas_terceiro_trimestre)

soma = np.array([media_primeiro_trimestre, media_segundo_trimestre, media_terceiro_trimestre])
media_final = np.mean(soma)
# 

print(f'Média final: {media_final:.1f}')
if media_final >= 7:
    print('Aprovado!!')
else:
    print('Reprovado!')
sl(3)

print('///')

print(f'Média do 1° trimestre: {media_primeiro_trimestre:.1f}')
print(f'Média do 2° trimestre: {media_segundo_trimestre:.1f}')
print(f'Média do 3° trimestre: {media_terceiro_trimestre:.1f}')