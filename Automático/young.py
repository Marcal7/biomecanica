import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def plot(df):

    phantoms = {
        "P_1": (0, 1),  # Índices para P_1
        "P_2": (3, 4),  # Índices para P_2
        "P_3": (6, 7),  # Índices para P_3
    }

    # Dicionário para armazenar os módulos de Young
    modulos_young = {}

    # Loop sobre cada phantom
    for nome, (c0, c1) in phantoms.items():
        strain = df.iloc[:, c0]
        stress = df.iloc[:, c1]

        # Converter para valores numéricos
        strain = pd.to_numeric(strain, errors='coerce')
        stress = pd.to_numeric(stress, errors='coerce')

        # Remover linhas com valores não numéricos
        df_plot = pd.DataFrame({'Strain': strain, 'Stress': stress}).dropna()

        # Realizar o ajuste linear
        slope, intercept, r_value, p_value, std_err = linregress(df_plot['Strain'], df_plot['Stress'])

        # O módulo de Young é dado pela inclinação do ajuste linear
        modulos_young[nome] = slope

        # Criar gráfico com o ajuste
        plt.plot(df_plot['Strain'], df_plot['Stress'], 'o', label=f'{nome} Dados')
        plt.plot(df_plot['Strain'], slope * df_plot['Strain'] + intercept, label=f'{nome} Ajuste', linestyle='--')

        # Adicionar título e exibir o gráfico
        plt.title('Ajuste Linear de Stress vs Strain para Diferentes Phantoms')
        plt.xlabel('Strain')
        plt.ylabel('Stress (Pa)')
        plt.legend()
        plt.show()

    # Exibir os módulos de Young calculados
    for nome, modulo in modulos_young.items():
        print(f'Módulo de Young para {nome}: {modulo:.2f} Pa')

