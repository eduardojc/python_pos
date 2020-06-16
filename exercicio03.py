'''
    Aluno: Eduardo Jose Christofoletti
    Turma: PÓS DATA SCIENCE UNIARARAS  (FHO)

     EXERCICIO:
         Crie um arquivo chamado “notas.txt” que contenha o nome de um aluno, e 6 notas
        (Ma1, Mb1, P1, Ma2, Mb2 e P2), com todos os dados separados por ‘,’ (vírgula).
        Escreva um programa em Python que faça a leitura desse arquivo e exiba na tela o
        nome do aluno e a média final, calculada a partir da fórmula a seguir:
'''

aluno = open('notas.txt')
lines = aluno.read().split(',')

a1 = (float(lines[3])*0.7) + float(lines[1])*0.1 + float(lines[2])*0.2
a2 = (float(lines[6])*0.7) + float(lines[4])*0.1 + float(lines[5])*0.2
nota_final = (a1+(2*a2))/3

print(nota_final)