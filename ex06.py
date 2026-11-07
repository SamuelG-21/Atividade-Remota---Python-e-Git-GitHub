#################################################################
#                                                               #
# Descrição: Faça um programa que apresente os quadrados dos    #
#            números inteiros na faixa de valores de 15 a 200.  #
#                                                               #
# Parâmetros de entrada: Nenhum (intervalo fixo de 15 a 200).     #
#                                                               #
# Valores de saída: O quadrado de cada número inteiro no        #
#                   intervalo especificado.                     #
#                                                               #
# Autor:         Samuel Guimarães Amorim                        #
#                                                               #
#################################################################

for i in range(15, 201):
    print(f"O quadrado de {i} é {i ** 2}")