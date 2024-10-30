import numpy as np
import scipy.io

# Parâmetros
dt = 0.0001  # Intervalo de tempo entre frames (s)
dx = 0.2977  # Resolução lateral (mm)
densidade = 900  # Densidade do material (kg/m³)

# Função para calcular a velocidade da onda de cisalhamento usando o tempo ao pico
def calcular_velocidade_onda_tempo_ao_pico(disp_map, dt, dx):
    num_frames = disp_map.shape[2]
    tempo_pico_por_coluna = np.zeros(disp_map.shape[1])

    for coluna in range(disp_map.shape[1]):
        deslocamento_temporal = disp_map[:, coluna, :]
        media_deslocamento_temporal = deslocamento_temporal.mean(axis=0)
        frame_pico = np.argmax(media_deslocamento_temporal)
        tempo_pico_por_coluna[coluna] = frame_pico * dt

    posicao_inicial = 0
    posicao_final = len(tempo_pico_por_coluna) - 1
    distancia_total = (posicao_final - posicao_inicial) * dx
    tempo_total = tempo_pico_por_coluna[posicao_final] - tempo_pico_por_coluna[posicao_inicial]
    velocidade_onda = distancia_total / tempo_total

    return velocidade_onda

# Função para calcular o módulo de Young a partir da velocidade da onda de cisalhamento
def calcular_modulo_de_young(velocidade_onda, densidade):
    velocidade_onda_m_s = velocidade_onda / 1000.0
    modulo_de_young = 3 * densidade * (velocidade_onda_m_s ** 2)
    return modulo_de_young

# Lista de caminhos para os arquivos dos phantoms
file_paths = [
    "SRF-SWE-Phantom_P_A.mat",
    "SRF-SWE-Phantom_P_B.mat",
    "SRF-SWE-Phantom_P_C.mat"
]

# Calcula e armazena os resultados para cada phantom
resultados = []

for file_path in file_paths:
    mat_data = scipy.io.loadmat(file_path)
    disp_map = mat_data['disp_map']

    velocidade_onda = calcular_velocidade_onda_tempo_ao_pico(disp_map, dt, dx)
    modulo_de_young = calcular_modulo_de_young(velocidade_onda, densidade)

    resultados.append({
        "file_path": file_path,
        "velocidade_onda": velocidade_onda,
        "modulo_de_young": modulo_de_young
    })

# Exibe os resultados
for i, resultado in enumerate(resultados, 1):
    print(f"Phantom {i}:")
    print(f"  Velocidade da onda de cisalhamento: {resultado['velocidade_onda']:.2f} mm/s")
    print(f"  Módulo de Young: {resultado['modulo_de_young']:.2f} Pa\n")
