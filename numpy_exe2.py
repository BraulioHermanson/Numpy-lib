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