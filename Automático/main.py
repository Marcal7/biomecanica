
import reader
import young
import deslocamento

'''Tensão  (stress) e deformação (strain) são conceitos importantes na engenharia e na ciência dos materiais. 
A diferença entre stress e deformação é que o stress é a força aplicada a um material por unidade de área, 
enquanto a deformação é a alteração na forma do material resultante da força aplicada.'''

# Módulo de Young --> E =  𝜎 / ε
# 𝜎 = Stress
# ε = Strain

def imagens(imgs):
    dados = {}
    reader.ler(imgs)

def planilha():
    return reader.xlsx('Tensão deformação.xlsx')

imgs = ['SRF-SWE-Phantom_P_A.mat', 'SRF-SWE-Phantom_P_B.mat', 'SRF-SWE-Phantom_P_C.mat']

df = planilha()
print(df)

young.plot(df)

imagens(imgs)


dist = 0.1
for img in imgs:
    deslocamento.calcular_velocidade(img, dist)







