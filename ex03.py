#################################################################
#                                                               #
# Descrição: Faça um Programa que verifique se uma letra digitada #
#            é "F" ou "M". Conforme a letra escrever: F -       #
#            Feminino, M - Masculino, Sexo Inválido.            #
#                                                               #
# Parâmetros de entrada: Uma letra (caractere) informada        #
#                        pelo usuário.                          #
#                                                               #
# Valores de saída: "F - Feminino", "M - Masculino" ou          #
#                   "Sexo Inválido".                            #
#                                                               #
# Autor:         Samuel Guimarães Amorim                        #
#                                                               #
#################################################################

letra = input('Digite uma letra: ').upper()
if letra == 'F':
    print('F - Feminino')
elif letra == 'M':
    print('M - Masculino')
else:
    print('Sexo inválido')