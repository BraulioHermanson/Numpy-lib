import numpy as np

vendas = np.array([200, 220, 250, 210, 300, 280, 230, 210, 220, 240, 230, 210, 280, 220])

vendas_reshaped = np.reshape(vendas, (2,7))
print(vendas_reshaped)
print('-'*20)
vendas_reshaped = np.reshape(vendas, (2, -1))
print(vendas_reshaped)
print('-'*20)
vendas_reshaped = np.reshape(vendas, (-1,7))
print(vendas_reshaped)
print('-'*20)
print('-'*20)

### """Considere que uma loja funciona de segunda a sabado,
# independente de feriados. Nos ultimos 30 dias, teve o menor volume de vendas sendo 20
# eo maior sendo 200. Crie uma simulação das vendas desses ultimos 30 dias, separando por semanas.
# Calcule o total de vendas por semana, a media de vendas por semana e a media de vendas por dia da semana"""

rng = np.random.default_rng(seed=42)
vendas = rng.integers(low=20, high=200, size=30,endpoint=True)
print(vendas)
vendas_semanais = np.reshape(vendas,(-1,6))
print(vendas_semanais)
print('-'*20)
rng = np.random.default_rng(seed=42)
vendas = rng.integers(low=20, high=200, size=(5,6),endpoint=True)
print(vendas)
print('-'*20)
# Total de vendas semana
rng = np.random.default_rng(seed=42)
vendas_semanais = rng.integers(low=20, high=200, size=(5,6),endpoint=True)
total_vendas_semanais = vendas_semanais.sum(axis=1)
print(total_vendas_semanais)
media_vendas_semanais = vendas_semanais.mean(axis=1)
print(media_vendas_semanais)
media_vendas_dia = vendas_semanais.mean(axis=0)
print(media_vendas_dia)
print('-'*20)
print('#'*20)
##"""Exercicio2 - Tem os dados de vendas de 3 produtos diferentes, para os ultimos 5 dias em um array 2D numpy.
# Cada linha do array representa um produto e cada coluna representa um dia. Seu trabalho é calcular as vendas totais para cada
# produtoe para cada dia."""

vendas = np.array([[50, 60, 70, 65, 80],
                  [85, 90, 78, 92, 88],
                  [72, 75, 68, 77, 76]])

vendas_produto = np.sum(vendas, axis=1)
print(vendas_produto)
print(f"Vendas totais do produto A: {vendas_produto[0]}")
print(f"Vendas totais do produto B: {vendas_produto[1]}")
print(f"Vendas totais do produto C: {vendas_produto[2]}")
print('#'*20)
vendas_dia = np.sum(vendas, axis=0)
print(vendas_dia)

for i in range(5):
    print(f"Vendas do dia {i+1}: {vendas_dia[i]}.")

print('#'*20)

## Exercicio 3 
rng = np.random.default_rng(seed=42)
respostas = rng.integers(low=0, high=10, size=210, endpoint=True)
print(respostas)
respostas_reshaped = np.reshape(respostas, (7,30))
print(respostas_reshaped)
print('-'*20)
media_geral = np.mean(respostas_reshaped)
print(media_geral)
media_diaria = np.mean(respostas_reshaped, axis=1)
print(media_diaria)
media_semanal = np.mean(respostas_reshaped, axis=0)
print(media_semanal)