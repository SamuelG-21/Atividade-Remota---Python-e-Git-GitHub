#################################################################
#                                                               #
# Descrição: Faça um Programa que peça um valor e mostre na     #
#            tela se o valor é positivo ou negativo.            #
#                                                               #
# Parâmetros de entrada: Um número inteiro ou real              #
#                        informado pelo usuário.                #
#                                                               #
# Valores de saída: Mensagem indicando se o número é            #
#                   positivo, negativo ou zero.                 #
#                                                               #
# Autor:         Samuel Guimarães Amorim                        #
#                                                               #
#################################################################

num = float(input('Digite um valor: '))
if num > 0:
    print(f'O número {num} é positivo')
elif num < 0:
    print(f'o número {num} é negativo')
else:
    print('O número 0 não é positivo nem negativo')




