# Escreva um programa que encontre as raízes da equação abaixo.
#  Os valores de A, B e C deverão ser solicitados ao usuário:



print("==========CALCULADORA DE BASKARA==========")
a = int(input('valor de A: '))
b = int(input('valor de B: '))
c = int(input('valor de C: '))

import math

delta = (b**2) - (4*a*c)
if delta > 0:
    raiz = math.sqrt(delta)
    raiz1 = (-b + raiz)/(2*a)
    raiz2 = (-b - raiz)/(2*a)
    print(f"As raizes da equação são: x1 = {raiz1} e x2 = {raiz2}")

if delta < 0:
    print('a equação não possuirá valores reais')

if delta == 0:
    raiz2 = (-b /(2*a))
    raiz1 = (-b /(2*a))
    print(f"\n\nDELTA = {delta} \n\nAs raizes da equação são: x1 = {raiz1} e x2 = {raiz2}")
