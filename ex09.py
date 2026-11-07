#################################################################
#                                                               #
# Descrição: Elabore um programa que apresente o somatório     #
#            dos valores pares existentes na faixa de 1 até 500.#
#                                                               #
# Parâmetros de entrada: Nenhum.                                #
#                                                               #
# Valores de saída: O somatório dos números pares entre 1 e 500.  #
#                                                               #
# Autor:         Samuel Guimarães Amorim                        #
#                                                               #
#################################################################

soma_pares = 0
for i in range(2, 501, 2):
    soma_pares += i

print(f"O somatório dos valores pares de 1 até 500 é: {soma_pares}")