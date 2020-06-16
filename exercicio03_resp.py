def calcula_a1_a2(prova_ind, av_ind, av_grupo):
    nota = (prova_ind*0.7) + (av_ind * 0.1) + (av_grupo * 0.2)
    return nota

def calcula_media(A1, A2):
    media = ( A1 + 2 * A2)/3
    return media


while True:

    while True:
        try:

            print('-'*30)
            print('1 - Inserir dados no arquivo')
            print('2 - Calcular Medias')
            print('3 - Sair')
            op = int(input('Informe a opcao desejada: '))
            break
        except ValueError:
            print('\n Favor informar um número.')

    if op == 1:
        try:
            file = open('notas.txt', 'a')
            nome =  input('Informe o nome do aluno: ')
            p1 = input('Informe a nota P1: ')
            ma1 = input('Informe a nota Ma1: ')
            mb1 = input('Informe a nota Mb1: ')
            p2 = input('Informe a nota P2: ')
            ma2 = input('Informe a nota Ma2: ')
            mb2 = input('Informe a nota Mb2: ')

            file.write('\n{},{},{},{},{},{},{}'.format(nome,p1,ma1,mb1,p2,ma2,mb2))
            file.close()
        except IOError:
            print('\n Erro ao abrir o arquivo!')
            break

        except IOError:
            print('\n Erro ao abrir o arquivo!')
    elif op == 2:
        try:
            file = open('notas.txt','r')
        except IOError:
            print('Erro ao abrir o arquivo!')
            break

        for linha in file:
            linha = linha.replace('\n','')
            linha = linha.split(',')

            nome = linha[0]
            p1 = float(linha[1])
            ma1 = float(linha[2])
            mb1 = float(linha[3])
            p2 = float(linha[4])
            ma2 = float(linha[5])
            mb2 = float(linha[6])

            A1 = calcula_a1_a2(p1, ma1, mb1)
            A2 = calcula_a1_a2(p2, ma2, mb2)

            media = calcula_media(A1, A2)
            print('Nome: {} - Media Final = {:.2f}'.format(nome, media))
        file.close()
    else:
        break