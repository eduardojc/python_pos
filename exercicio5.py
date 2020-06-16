'''
    Aluno: Eduardo Jose Christofoletti
    Turma: PÓS DATA SCIENCE UNIARARAS  (FHO)

     EXERCICIO:
        Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a
        um grande quantidade de organizações:
'''


print('Qual o melhor Sistema Operacional para uso em servidores?')
print('1- Windows Server, 2- Unix, 3- Linux, 4- Netware, 5- Mac OS, 6- Outro','0 - Para encerrar a Enquete')

so = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']

sistemas = [0] * 6
while True:
    while True:
        opcao = int(input('Digite a opção para votar: '))
        if opcao > 6 or opcao < 0:
            print('Opção digitada é inválida.')
        else:
            break
    if opcao == 0:
        break
    sistemas[opcao - 1] = sistemas[opcao - 1] + 1


print('Sistema Operacional     Votos  %')
print('----------------------------------')
cont = 0
melhor = 0
melhorSis = ''
qtd = 0
for sis in sistemas:
    print('%s           %d    %.2f%%' % (so[cont], sis,(sis * 100) / sum(sistemas) ))
    if sis > melhor:
        melhor = sis
        melhorSis = so[cont]
        qtd = (sis * 100) / sum(sistemas)
    cont += 1

print('----------------------------------')
print('Total                          %d' % sum(sistemas))
print('O Sistema Operacional mais votado foi o %s, com %d votos, correspondendo a %.2f dos votos.' % (melhorSis, melhor, qtd))

