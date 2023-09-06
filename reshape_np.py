import numpy as np

vendas = np.array([200, 220, 250, 210, 300, 280, 230, 210, 220, 240, 230, 210, 280, 220])

vendas_reshaped = np.reshape(vendas, (2,7))
print(vendas_reshaped)
print(vendas.ndim)
print(vendas.shape)
print(vendas_reshaped.ndim)
print(vendas_reshaped.shape)
print(vendas_reshaped[0])
print(vendas_reshaped[0][4])
print(vendas_reshaped.sum())
print('-'*20)
print(vendas_reshaped)
print('#'*20)
print(f"Soma eixo zero - {vendas_reshaped.sum(axis=0)}")
print(f"Soma eixo um - {vendas_reshaped.sum(axis=1)}")
print(f"Mediaa eixo um - {vendas_reshaped.mean(axis=1)}")