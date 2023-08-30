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