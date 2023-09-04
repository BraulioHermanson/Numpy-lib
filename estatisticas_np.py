import numpy as np

rng = np.random.default_rng()
print(rng)
numero_aleatorio = rng.random() *10
print(numero_aleatorio)
print('-'*20)
array_aleatorio = rng.random(3) * 100
print(array_aleatorio)
print('-'*20)
dados_vendas = rng.integers(low=50, high = 200, size =30)
print(dados_vendas)
print('-'*20)

rng = np.random.default_rng(seed = 42) # o seed mantem o msm numero que outra pessoa rodar o codigo
dados_vendas = rng.integers(low=50, high = 200, size =30)
print(dados_vendas)
print('-'*20)
print(np.max(dados_vendas))
#argmax/argmin - pega a numeracao do array
print(np.argmax(dados_vendas) + 1) # +1 serve para comecar a contagem no 1
print(np.argmin(dados_vendas) + 1)
print(f"Dias com mais vendas: {np.argmax(dados_vendas) + 1}")
print(f"Dias com menos vendas: {np.argmin(dados_vendas) + 1}")
print('-'*20)

#funcoes estatisticas
media_vendas = np.mean(dados_vendas)
print(f" A media de vendas foi {media_vendas}")
print(np.median(dados_vendas))
print(np.percentile(dados_vendas, 50))
print(f"{np.std(dados_vendas):.2f}")
print(f"{np.var(dados_vendas):.2f}")
print('-'*20)