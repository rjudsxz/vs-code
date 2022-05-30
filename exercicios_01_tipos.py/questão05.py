from random import sample
valor = tuple(sample(range(10), 5))
print(valor)
print(f'Maior valor é: {max(valor)}\nMenor valor é: {min(valor)}.')
