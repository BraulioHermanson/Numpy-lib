import numpy as np

array = np.array([1,2,3,4,5])
print(array)
print('-'*20)
## diferenca entre lista e array
# """Lista e uma estrutura de dados mais basicas do Python,
# podendo conter qualquer tipo de elemento, como numeros, string, 
# outras listas e toso elementos pode ser de tipos diferentes."""

lista = [1 , "dois" , 3.0]
print(type(lista))

for elemento in lista:
    print(type(elemento))

print('-'*20)
# """Um array é uma estrutura de dados que tambem armazena elementos, mas todos os elementos devem ser do mesmo tipo.
# Ao tentar criar um array com elementos de tipos diferentes o Numpy irá converte-los para o tipo mais geral"""

array = np.array(lista)
print(array)
print('-'*20)
print(type(array))
for elemento in array:
    print(type(elemento))

print(array.dtype)
print('-'*20)

# Operacoes Matematicas
lista = [1, 2, 3, 4, 5]
# nova_lista = lista +1 # gera erro no numpy

nova_lista = []
for numero in lista:
    nova_lista.append(numero + 1)

print(nova_lista)
print('-'*20)
## """Com o array do Numpy é possivel adicioanr(subtrair, multiplicar e dividir)
#  um numero a todos os elementos de uma vez"""

array = np.array([1, 2, 3, 4, 5])
novo_array = array+1
print(novo_array)

novo_array_ = array**2
print('-'*20)
print(novo_array_)
# Desempenho
# """Grandes quantidades de dados, os arrays NumPy sao signficativamente mais eficientes
#  em termos de memória e desempenho do que as listas"""

import numpy as np
import time

# Crie uma lista e um array com 10 milhões de números
lista = list(range(1, 10_000_001))
array = np.array(range(1, 10_000_001))

# Calcule a soma de todos os números na lista
inicio = time.time()
soma_lista = sum(lista)
fim = time.time()
print(f"Tempo para somar todos os números na lista: {fim - inicio} segundos")

# Calcule a soma de todos os números no array
inicio = time.time()
soma_array = np.sum(array)
fim = time.time()
print(f"Tempo para somar todos os números no array: {fim - inicio} segundos")

## """Resumindo
# 
#   Diferenças de listas e arrays
# 1- Tipo de dados
# 2- Operaçao  matematica
# """
