#################################################################
#                                                               #
# Descrição: Faça um Programa que peça dois números e imprima   #
#            o maior deles.                                     #
#                                                               #
# Parâmetros de entrada: Dois números inteiros ou reais         #
#                        informados pelo usuário.               #
#                                                               #
# Valores de saída: O maior número entre os dois digitados.     #
#                                                               #
# Autor:         Samuel Guimarães Amorim                        #
#                                                               #
#################################################################

num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))
if num1 > num2:
    print(f'O maior número digitado foi: {num1}')
elif num2 > num1:
    print(f'O maior número digitado foi: {num2}')
else:
    print('Os números são iguais')