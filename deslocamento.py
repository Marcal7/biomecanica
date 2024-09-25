import scipy.io
import numpy as np


def calcular_velocidade(img, distancia):
    # Carregar o arquivo .mat
    mat_data = scipy.io.loadmat(img)
    disp_map = mat_data['disp_map']

    # Parâmetros
    taxa_amostragem = 10000  # frames por segundo
    dt = 1 / taxa_amostragem  # intervalo de tempo em segundos

    # Armazenar tempos de pico e velocidades
    tempos_pico = []
    velocidades = []

    # Calcular o tempo ao pico para cada coluna
    for col in range(disp_map.shape[1]):
        # Identificar o índice do pico
        pico_index = np.argmax(disp_map[:, col, :])
        tempo_pico = pico_index * dt

        # Calcular a velocidade
        velocidade = distancia / tempo_pico if tempo_pico > 0 else 0

        # Armazenar resultados
        tempos_pico.append(tempo_pico)
        velocidade.append(velocidade)

    # Exibir resultados
    for i, v in enumerate(velocidade):
        print(f'Coluna {i}: Velocidade da onda de cisalhamento = {v:.2f} m/s')

    return tempos_pico, velocidade

