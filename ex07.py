#################################################################
#                                                               #
# Descrição: Elabore um programa que mostre os resultados da    #
#            tabuada de um número qualquer, o qual deve ser     #
#            apresentado de acordo com a sua forma tradicional. #
#                                                               #
# Parâmetros de entrada: Um número inteiro informado pelo       #
#                        usuário para gerar a tabuada.          #
#                                                               #
# Valores de saída: Tabuada do número de 1 a 10 formatada.      #
#                                                               #
# Autor:         Samuel Guimarães Amorim                        #
#                                                               #
#################################################################

numero = int(input("Digite um número para ver a tabuada: "))

print(f"--- Tabuada do {numero} ---")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")