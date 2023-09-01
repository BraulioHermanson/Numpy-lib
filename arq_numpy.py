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
# 1 - Tipo de dados
# 2 - Operaçao  matematica
# 3 - Desempenho
# 4 - Funcionalidades """

## ARRAYS
# É uma estrutura de dados que armazena valores do mesmo tipo. Em Python, isso é uma grande vantagem,pq economiza espaço e permite operaçoes mais eficientes

array = np.array(["a", "b", "c", "d", "e"])
print(array)
# indexacao e slice
print('-'*20)
print(array[0])
print(array[1:4])
print(array[0:-1])
# step
print(array[0:-1:2])
# :: inclui a ultima letra
print(array[0::2])
print(array[::2])
print(array[::])
print(array[::-1])
print('-'*20)
# aplicacoes do dia dia
precos = np.array([20, 25, 30, 35, 40])
#auntemando os precos em 10%
novos_precos = precos *1.1
print(novos_precos)

#np.sum()
vendas = np.array([200, 220, 250, 210, 300])
print(np.sum(vendas))

# np.mean()
vendas = np.array([200, 220, 250, 210, 300, 280, 230])
media_vendas = np.mean(vendas)
print(f"A media de vendas foi: {media_vendas:.2f}.")

#np.max() np.min()
precos = np.array([20, 25, 30, 35, 40])
produto_mais_caro = np.max(precos)
produto_mais_barato = np.min(precos)
print(f"Produto mais caro: {produto_mais_caro}")
print(f"Produto mais barato: {produto_mais_barato}")

#np.sort()
vendas = np.array([200, 220, 250, 210, 300])
print(np.sort(vendas))

#np.dot()
# usado para calcular o produto escalar de dois arrays.
# Calcular o valor total de vendas, dado o numero da cada produto vendido e o preco de cada produto

quantidades = np.array([10, 20, 30, 40])
precos_unitarios = np.array([5, 10, 15, 20])

print(quantidades* precos_unitarios)
print(np.sum(quantidades* precos_unitarios))
print(np.dot(quantidades, precos_unitarios))