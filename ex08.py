#################################################################
#                                                               #
# Descrição: Construir um programa que apresente a soma dos     #
#            cem primeiros números (1+2+3+...+50+...+100).      #
#                                                               #
# Parâmetros de entrada: Nenhum.                                #
#                                                               #
# Valores de saída: O valor total da soma de 1 até 100.         #
#                                                               #
# Autor:         Samuel Guimarães Amorim                        #
#                                                               #
#################################################################

soma = 0
for i in range(1, 101):
    soma += i

print(f"A soma dos cem primeiros números é: {soma}")