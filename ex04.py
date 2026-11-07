#################################################################
#                                                               #
# Descrição: Faça um Programa que pergunte em que turno você    #
#            estuda. Peça para digitar M-Matutino ou            #
#            V-Vespertino ou N-Noturno. Imprima a mensagem      #
#            "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou        #
#            "Valor Inválido!", conforme o caso.                #
#                                                               #
# Parâmetros de entrada: Uma letra correspondente ao turno      #
#                        (M, V ou N).                           #
#                                                               #
# Valores de saída: Saudação correspondente ou "Valor           #
#                   Inválido!".                                 #
#                                                               #
# Autor:         Samuel Guimarães Amorim                        #
#                                                               #
#################################################################

turno = input("Em que turno você estuda? (Digite M para Matutino, V para Vespertino ou N para Noturno): ").strip().upper()

if turno == 'M':
    print("Bom Dia!")
elif turno == 'V':
    print("Boa Tarde!")
elif turno == 'N':
    print("Boa Noite!")
else:
    print("Valor Inválido!")