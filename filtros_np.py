import numpy as np

salarios = np.array([3000, 3500, 4000, 2000, 4500, 4000, 5000])

media_salarial = np.mean(salarios)

print(f"{media_salarial:.2f}")

acima = np.where(salarios > media_salarial)
print(acima)
print(salarios[acima])
print(salarios[salarios> media_salarial])
print(salarios[salarios >= 6000])
print('-'*20)
print(np.where(salarios > media_salarial, "Acima da media", "Abaixo da media"))

salarios_bonus = np.where(salarios > media_salarial, salarios*1.1, salarios)
print(salarios_bonus)
print('-'*20)
print(np.where((salarios>= 3000) & (salarios<=4500)))

salarios_ajustados = np.where((salarios>= 3000) & (salarios<=4500), salarios *1.05, salarios)
print(salarios_ajustados)
print(np.where((salarios_ajustados < 3000) | (salarios_ajustados > 4500)))
salarios_seg_ajustes = np.where((salarios_ajustados < 3000) | (salarios_ajustados > 4500),salarios_ajustados*1.1, salarios_ajustados)
print(salarios_seg_ajustes)
