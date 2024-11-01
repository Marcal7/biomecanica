---

# Análise de Modulo de Young e Cisalhamento com Mapas de Deslocamento de Phantoms

---

## Resumo em Português
Este projeto calcula a velocidade de propagação da onda de cisalhamento e módulos de Young e cisalhamento em diferentes phantoms, armazenados em arquivos `.mat`. O arquivo principal `teste.ipynb` contém a implementação e análise visual.

## Summary in English
This project calculates shear wave velocity and Young’s and shear moduli across different phantoms stored in `.mat` files. The main notebook `teste.ipynb` holds the implementation and visualization analysis.

---

## Descrição
Este projeto visa calcular a velocidade de propagação da onda de cisalhamento e os módulos de Young e de cisalhamento em diferentes phantoms utilizando mapas de deslocamento gerados por ultrassom. Cada phantom foi submetido a um pulso acústico focalizado e o deslocamento da onda foi registrado ao longo de 148 frames, permitindo cálculos precisos sobre as propriedades do material.

> **Arquivo principal**: O código completo de análise está no notebook **`NotebookGraficos -> teste.ipynb`**. Este é o arquivo principal onde o cálculo de velocidade da onda, módulo de Young e cisalhamento são realizados, bem como os gráficos ilustrativos.

---

## Estrutura do Projeto
  - `NotebookGraficos/`
    - `teste.ipynb` – Notebook principal com a execução do código de análise.
  - Dados (`.mat` e `.xlsx`) – Contêm os mapas de deslocamento e dados auxiliares para o cálculo.

## Resumo dos Cálculos
### Descrição dos Mapas de Deslocamento
Os mapas de deslocamento (`disp_map`) são tridimensionais, com dimensões 162x128x148. Cada arquivo contém:
- Resolução lateral de 38,4 mm (`dx = 0,2977 mm`)
- Resolução axial de 15 mm (`dz = 0,1885 mm`)

Esses dados permitem um cálculo preciso da onda de cisalhamento utilizando a técnica de tempo ao pico, que identifica o tempo necessário para a onda atingir diferentes posições.

### Cálculo da Velocidade de Onda e Módulos de Young e Cisalhamento
Através dos mapas de deslocamento, foi possível calcular:
- **Velocidade da onda de cisalhamento**: Razão entre distância e tempo para o deslocamento da onda.
- **Módulo de Young** e **módulo de cisalhamento**: Calculados com base na densidade do material e velocidade da onda.

## Instalação e Uso

### Pré-requisitos
Para rodar o código, instale as bibliotecas necessárias:
```bash
pip install numpy pandas matplotlib scipy openpyxl
```

### Execução
1. Coloque os arquivos `.mat` e a planilha `.xlsx` na pasta do projeto.
2. Execute o notebook `teste.ipynb`, que realiza o carregamento de dados, processamento dos cálculos, e geração dos gráficos.

## Exemplos de Uso
O exemplo a seguir mostra como definir os caminhos das imagens e como calcular os valores para cada phantom.

```python
# Definir caminhos das imagens
imgs = [
    'SRF-SWE-Phantom_P_A.mat',
    'SRF-SWE-Phantom_P_B.mat',
    'SRF-SWE-Phantom_P_C.mat'
]

# Realizar cálculos para cada phantom
for img in imgs:
    mat_data = scipy.io.loadmat(img)
    disp_map = mat_data['disp_map']
    velocidade_media, modulo_young, modulo_cisalhamento, velocidade_onda = calculos(disp_map)
    print(f"Resultados para {img}: Velocidade média = {velocidade_media:.2f} m/s, Módulo de Young = {modulo_young:.2f} Pa")
```

## Resultados
O notebook exibe gráficos comparativos dos módulos de Young entre os phantoms. Este é um exemplo ilustrativo para a compreensão visual dos resultados.
