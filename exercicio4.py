'''
    Aluno: Eduardo Jose Christofoletti
    Turma: PÓS DATA SCIENCE UNIARARAS  (FHO)

     EXERCICIO:
         Crie um arquivo chamado “notas.txt” que contenha o nome de um aluno, e 6 notas
        (Ma1, Mb1, P1, Ma2, Mb2 e P2), com todos os dados separados por ‘,’ (vírgula).
        Escreva um programa em Python que faça a leitura desse arquivo e exiba na tela o
        nome do aluno e a média final, calculada a partir da fórmula a seguir:
'''

file = open('notas.txt','a+')

nome = input('Digite seu Nome: ')
ma1 = input("Digite a nota Ma1: ")
mb1 = input("Digite a nota Mb1: ")
p1 = input("Digite a nota P1: ")
ma2 = input("Digite a nota Ma2: ")
mb2 = input("Digite a nota Mb2: ")
p2 = input("Digite a nota P2: ")

file.write('\n' + nome + ',' + ma1 + ',' + mb1 +',' + p1 +',' + ma2 + ',' + mb2 + ',' + p2)
file.close()

file = open('notas.txt')
lines = file.readline().replace('\n','')
lines = lines.split(',')

a1 = (float(lines[3])*0.7) + float(lines[1])*0.1 + float(lines[2])*0.2
a2 = (float(lines[6])*0.7) + float(lines[4])*0.1 + float(lines[5])*0.2
nota_final = (a1+(2*a2))/3

print(nota_final)