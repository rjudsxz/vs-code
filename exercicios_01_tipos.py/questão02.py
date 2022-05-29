# Escreva um programa para ler o número total de eleitores de um município, 
# o número de votos brancos e o número de votos nulos.
#  Considerando que todos os eleitores compareceram à votação, 
# o programa deve calcular o percentual dos votos apurados (válidos, brancos e nulos)

all = int(input('numero de eleitores: '))
validos = 0
brancos = 0
nulos = 0 


for votos in range(all):
    entrada = input(f'\n|========================================\n|Votar em candidatos: 1\n|Votar branco: 2\n|Votar nulo: 3\n========================================\n ')
    if entrada == "1":
        validos = validos + 1
    elif entrada == "2":
        brancos = brancos + 1
    if entrada == "3":
        nulos = nulos + 1

calculo_validos = (validos*100)/all
calculo_brancos = (brancos*100)/all
calculo_nulos = (nulos*100)/all

print(f'|========================================\n|APURAÇÃO DE 100% DOS VOTOS\n|========================================\n|Votos válidos {calculo_validos}%\n|Votos brancos {calculo_brancos}%\n|votos nulos {calculo_nulos}%\n|========================================')
