import numpy as np

# Ex 1 - O gerente de vendas tem os dados de vendas de um produto para os ultimos 7 dias na lista apresentada, calcule a media de vendas durante a semana

dados = [127, 90, 201, 150, 210, 220, 115]

media_semana = np.mean(dados)
print(media_semana)
print('-'*20)
# Ex 2 - Calcule o maximo, minimo e a variacao de precos durante a semana do array com os precos abaixo

precos = np.array([31.40, 31.25, 30.95, 31.20, 31.60, 31.50])

preco_max = np.max(precos)
preco_min = np.min(precos)
preco_var = preco_max - preco_min
print(f"Tivemos uma variacao de {preco_var:.2f}, contendo a maxima de {preco_max:.2f} e minima de {preco_min:.2f}")

"""# Ex 3 - A loja vendeu em um dia 5 unidades do Produto A,
 3 unidades do Produto B e 2 Unidades do Produto C. Os precos dos produtos sao, respectivamente,
 100, 200 e 50 reais, Calcule o total de vendas do dia"""

quantidade = np.array([5, 3, 2])
preco = np.array([100, 200, 50])
print(np.dot(quantidade,preco))

