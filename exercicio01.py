'''
    Aluno: Eduardo Jose Christofoletti
    Turma: PÓS DATA SCIENCE UNIARARAS  (FHO)

    EXERCICIO:
      Faça um programa em Python que recebe uma string que representa uma cadeia
        de DNA e gera a cadeia complementar.
'''


dna = input('Digite a cadeia de DNA: ')
print('Cadeia digitada: {}'.format(dna.upper()))
print('Gerando cadeia complementar...')
dna = dna.upper()
rna = dna.replace('T','a')
rna = rna.replace('A','t')
rna = rna.replace('C','g')
rna = rna.replace('G','c')
rna = rna.upper()
print('Cadeia complementar: {}'.format(rna.upper()))