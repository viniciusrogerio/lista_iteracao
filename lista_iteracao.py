#1. Faça uma função dados um texto e um inteiro n, exiba o texto n vezes.

def exibetexto(texto,n):
    i=0
    while i<n:
        print(texto)
        i+=1

#2. Faça um programa que fica solicitando um número ao usuário e o exiba. O programa deve
#ficar executando enquanto o usuário não digitar ‘sair’. 

def exibenumero(num):
    if num!='sair':
        print(num)
        while (num!='sair'):
            num=input('Digite um número: ')
            if num=='sair':
                break
            else:
                print(int(num))

#3. Faça uma função que dada uma string, exiba apenas os caracteres presentes em um índice
#par.

def exibecaracteres(string):
    for i in range(0,len(string)):
        if i%2==0:
            print (string[i],end=' ')
            
'''4. Faça uma função que dado um número n exiba o seguinte padrão.
1
2 2
3 3 3
4 4 4 4
.....
n n n n n n ... n'''

def exibepadrao(n):
    for i in range (n+1):
        for j in range (i):
            print(i,end=' ')
        print()

#5. Faça uma função que dado uma lista de números inteiro, exiba somente aqueles que são
#pares e múltiplos de 2 e 3.

def exibemultiplos(lista):
    for i in lista:
        if i%2==0 and i%3==0:
            print (i,end=' ')

#6. Faça uma função que dado um número inteiro N, exiba todos os números até N que são
#pares e múltiplos de 2 e 3.

def exibemultiplos_ate(n):
    for i in range(n+1):
        if i%2==0 and i%3==0:
            print (i,end=' ')
            
#7. Faça uma função que dado um número inteiro N, retorne o somatório de todos os números
#até N que são pares e múltiplo de 2 ou 3, mas não de ambos simultaneamente.

            
def retornasomatorio(n):
    somatorio=0
    for i in range(n+1):
        if i%2==0:
            if (i%2==0 or i%3==0) and not (i%2==0 and i%3==0):
                somatorio+=i
    return somatorio

'''8. Dadas duas listas, por exemplo :
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
Escreva uma função que retorne uma lista que contenha apenas os elementos comuns entre as
listas (sem duplicatas). '''

def retornalista(a,b):
    lista_final=[]
    for i in a:
        if (i in b) and (i not in lista_final):
            lista_final.append(i)
    return lista_final

'''9. Faça o jogo pedra-papel-tesoura contra o computador. A entrada da função é um inteiro, tal
que 1 = ‘pedra’; 2 = ‘papel’ e 3 = ‘tesoura’. Nesse jogo, o resultado é empate se ambos
escolherem o mesmo artefato.
Papel ganha de pedra;
Tesoura ganha de papel e
Pedra ganha de tesoura.
O jogo deverá continuar sua execução enquanto não for digitado -1. Ao digitar -1, deve-se
exibir quantas rodadas foram executadas, quantas vitórias foram do usuário, quantas vitórias
foram do computador e quantos empates ocorreram.
Dica: use o módulo random em python ou a função random dos pascalzim'''

from random import randint
def jokenpo(op):
    op=int(op)
    
    num_rodadas=0
    num_vitorias=0
    num_derrotas=0
    num_empates=0
    
    
    ja_executou=False
    
    if op == -1:
        print('O jogo não será executado pois o usuário digitou -1.')
    while(op!=-1):
        if(ja_executou):
            op=int(input('Digite a opção: '))
        if op == -1:
            print('Foram feitas {} rodadas. O Usuário venceu {}, o Computador venceu {} e houveram {} empates.'.format(num_rodadas,num_vitorias,num_derrotas,num_empates))
            break
        else:
            if op == 1 or op == 2 or op == 3:
                ja_executou=True
                num_rodadas+=1
                comp=randint(1,4)
                
                if op == comp:
                    num_empates+=1
                    print('Empate!')
                    print()
                else:
                    if op == 1:
                        print('Usuário escolheu pedra.')
                        if comp == 2:
                            print('Computador escolheu papel.')
                            user_wins=False
                        else:
                            print('Computador escolheu tesoura.')
                            user_wins=True
                    elif op == 2:
                        print('Usuário escolheu papel.')
                        if comp == 1:
                            print('Computador escolheu pedra.')
                            user_wins=True
                        else:
                            print('Computador escolheu tesoura.')
                            user_wins=False
                    else:
                        print('Usuário escolheu tesoura.')
                        if comp == 1:
                            print('Computador escolheu pedra.')
                            user_wins=False
                        else:
                            print('Computador escolheu papel.')
                            user_wins=True
                    if (user_wins):
                        num_vitorias+=1
                        print('Você venceu !!!')
                        print()
                    else:
                        num_derrotas+=1
                        print('O computador venceu. Tente outra vez :(')
                        print()
            else:
                print('Opção inválida!')
                ja_executou=True
                print()

'''10. Faça uma função que dado um vetor(lista) de 10 posições deve retornar uma nova lista
com os valores de cada posição do vetor(lista) fazendo um shift para a direita. Além disso, o
vetor(lista) deve ser considerado circular, ou seja, o valor da última célula passa a ser o
valor(lista) da primeira. Exemplo:
Vetor(lista) original: [2, 1, 20, 5, 17, 19, 14, 4, 18, 5]
Vetor(lista) manipulado: [5, 2, 1, 20, 5, 17, 19, 14, 4, 18]'''

def shift(lista):
    lista_final=[0]
    lista_final[0]=lista[-1]
    for i in range (0,len(lista)-1):
        lista_final.append(lista[i])
    return lista_final