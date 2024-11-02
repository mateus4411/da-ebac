import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv')

sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))

grafico = sns.lineplot(data=df, x='dia', y='venda', marker='o', color="b", label="Vendas de gasolina")

plt.title('Vendas Diárias de Gasolina', fontsize=16)
plt.xlabel('Dia', fontsize=14)
plt.ylabel('Venda (litros)', fontsize=14)

plt.savefig('gasolina.png', dpi=300)

plt.legend(title='Legenda')

plt.show()
