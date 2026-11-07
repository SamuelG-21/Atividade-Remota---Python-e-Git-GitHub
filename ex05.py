#################################################################
#                                                               #
# Descrição: Faça um programa para a leitura de duas notas      #
#            parciais de um aluno. O programa deve calcular     #
#            a média alcançada por aluno e apresentar:          #
#            - A mensagem "Aprovado", se a média alcançada      #
#              for maior ou igual a sete;                       #
#            - A mensagem "Reprovado", se a média for menor      #
#              do que sete;                                     #
#            - A mensagem "Aprovado com Distinção", se a média   #
#              for igual a dez.                                 #
#                                                               #
# Parâmetros de entrada: Duas notas parciais (float).           #
#                                                               #
# Valores de saída: Média e a situação do aluno conforme        #
#                   as regras.                                  #
#                                                               #
# Autor:         Samuel Guimarães Amorim                        #
#                                                               #
#################################################################

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print(f"Média alcançada: {media:.2f}")

if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")