'''
    Aluno: Eduardo Jose Christofoletti
    Turma: PÓS DATA SCIENCE UNIARARAS  (FHO)

    EXERCICIO:
        Um anagrama é uma palavra que é feita a partir da transposição das letras de
        outra palavra ou frase. Por exemplo, “Iracema” é um anagrama de “América”.
        Escreva um programa em Python que decida se uma string é um anagrama de outra
        string, ignorando os espaços em branco. O programa deve considerar maiúsculas e
        minúsculas como sendo caracteres iguais, ou seja, “a” = “A”.
'''


s1 = input('Digite a primeira string: ')
s2 = input('Digite a segunda string: ')

def solucaoAnagrama(s1,s2):
    umalista1 = list(s1)
    umalista2 = list(s2)

    umalista1.sort()
    umalista2.sort()

    pos = 0
    iguais = True

    while pos < len(s1) and iguais:
        if umalista1[pos]==umalista2[pos]:
            pos = pos + 1
        else:
            iguais = False

    return iguais

if solucaoAnagrama(s1,s2) == True:
    print('São anagramas!')
else:
    print('Não são anagramas')

