# Faça um programa que leia o nome completo de uma pessoa
#  mostrando em seguida o primeiro e último nome separadamente
n = str(input('Digite o seu nome completo: '))

nome = n.split()
print('Primeiro nome é: {}'.format(nome[0]))

print('O seu ultimo nome é: {}'.format(nome[len(nome) - 1]))
