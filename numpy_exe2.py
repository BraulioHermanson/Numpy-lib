import numpy as np

# """Identifique quantas pessoas ganham acima da media com o array apresentado"""
salarios = np.array([3000, 2500, 3500, 4000, 2000, 4500, 3000, 3800, 4800])
media_salarial = np.mean(salarios)

resultado = np.where(salarios > media_salarial)
print(resultado)
print(salarios[salarios > media_salarial])
print(f"{np.sum(salarios>media_salarial)} possuem salarios acima da media.")
print('-'*20)
print(np.count_nonzero(salarios> media_salarial))
print(np.unique(salarios > media_salarial))
print(np.unique(salarios > media_salarial, return_counts=True))

valores_unicos, contagem = np.unique(salarios > media_salarial, return_counts=True)
print(valores_unicos)
print(contagem)
print('-'*20)

# """Criando 20 valores ficticios de salarios com a mesma faixa anterior,
#  tomando cuidado de outras pessoas gerarem os mesmos valores"""

rng = np.random.default_rng(seed=42)
salarios_gerados = rng.integers(low=np.min(salarios), high = np.max(salarios), size = 20)
print(salarios_gerados)
salarios_gerados = rng.integers(low=np.min(salarios), high = np.max(salarios), size = 20, endpoint=True)
print(salarios_gerados)
print(np.mean(salarios_gerados))
print(salarios_gerados.min())
print(salarios_gerados.max())
print(salarios_gerados.mean())

print('-'*20)
print('#'*20)
tempos_ciclo = np.array([5.5, 5.7, 5.9, 6.0, 5.8, 5.6, 5.7, 7.2, 4.8])
media = np.mean(tempos_ciclo)
print(media)
desvio_padrao = np.std(tempos_ciclo)
print(desvio_padrao)
print(f"Valores abaixo, ate 2 desvio: {media-2*desvio_padrao:.2f}\ne Valores acima, ate 2 desvio: {media+desvio_padrao*2:.2f}.")
condicao = (tempos_ciclo > media + 2*desvio_padrao) | (tempos_ciclo < media - 2*desvio_padrao)
anomalias = np.where(condicao)
print(anomalias)
print(tempos_ciclo[anomalias])

condicao = (tempos_ciclo > media + 2*desvio_padrao) | (tempos_ciclo < media - 2*desvio_padrao)
print(condicao)
print(np.where(condicao))
print('#'*20)
contrario_condicao = ((tempos_ciclo <= media + 2*desvio_padrao) & (tempos_ciclo >= media - 2*desvio_padrao))
print(np.where(contrario_condicao))
print(np.where(~condicao))

rng = np.random.default_rng(seed=0)
tempos_gerados = rng.normal(loc=media, scale= desvio_padrao, size=100)
print(tempos_gerados)
print(media)
print(tempos_gerados.mean())
print(desvio_padrao)
print(tempos_gerados.std())
condicao = ((tempos_gerados> tempos_gerados.mean() + 2*tempos_gerados.std()) | (tempos_gerados < tempos_gerados.mean() - 2*tempos_gerados.std()))
print(np.where(condicao))
print(tempos_gerados[condicao])