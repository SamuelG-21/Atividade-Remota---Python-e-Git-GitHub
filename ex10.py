#################################################################
#                                                               #
# Descrição: Elaborar um programa que apresente todos os        #
#            valores numéricos inteiros ímpares situados na     #
#            faixa de 0 a 20. Sugestão: para verificar se um    #
#            número é impar, dentro do laço de repetição,       #
#            fazer a verificação lógica dessa condição com a    #
#            instrução se/fimse dentro do próprio laço,         #
#            perguntando se o valor numérico do contador        #
#            é impar (se o resto da divisão por 2 for diferente #
#            de zero); sendo, mostre-o, não sendo, passe para   #
#            o próximo valor numérico. Para saber se um valor   #
#            numérico é ímpar, usar o método de cálculo do      #
#            divisibilidade por 2.                              #
#                                                               #
# Parâmetros de entrada: Nenhum.                                #
#                                                               #
# Valores de saída: Todos os números ímpares entre 0 e 20.        #
#                                                               #
# Autor:         Samuel Guimarães Amorim                        #
#                                                               #
#################################################################

print("Números ímpares de 0 a 20:")
for i in range(0, 21):
    if i % 2 != 0:
        print(i)