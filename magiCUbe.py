import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Definir as arestas do cubo
vertices = [
    [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],  # Base (z = 0)
    [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1],  # Topo (z = 1)
]

# Definir as faces do cubo (com cores RGB)
faces = [
    [vertices[0], vertices[1], vertices[5], vertices[4]],  # Face traseira
    [vertices[1], vertices[2], vertices[6], vertices[5]],  # Face direita
    [vertices[2], vertices[3], vertices[7], vertices[6]],  # Face frontal
    [vertices[3], vertices[0], vertices[4], vertices[7]],  # Face esquerda
    [vertices[0], vertices[3], vertices[2], vertices[1]],  # Base
    [vertices[4], vertices[5], vertices[6], vertices[7]],  # Topo
]

# Cores RGB para cada face do cubo
colors = [
    (1, 0, 0),  # Vermelho
    (0, 1, 0),  # Verde
    (0, 0, 1),  # Azul
    (1, 1, 0),  # Amarelo
    (1, 0, 1),  # Magenta
    (0, 1, 1),  # Ciano
]

# Configurar a figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Adicionar as faces ao cubo
poly3d = Poly3DCollection(faces, facecolors=colors, linewidths=1, edgecolors='r')
ax.add_collection3d(poly3d)

# Configurar os limites dos eixos
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])

# Adicionar rótulos aos eixos
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_zlabel('Eixo Z')

# Função para lidar com eventos de clique
def on_pick(event):
    if isinstance(event.artist, Poly3DCollection):
        # Obter as coordenadas do ponto clicado
        x, y, _ = event.mouseevent.xdata, event.mouseevent.ydata, event.mouseevent.zdata
        print(f'Coordenadas do ponto clicado: ({x:.2f}, {y:.2f})')

        # Encontrar a face clicada
        face_id = poly3d.get_facecolors().tolist().index(event.artist.get_facecolor().tolist())
        print(f'Cor da face clicada: {colors[face_id]}')

# Conectar a função de clique ao evento pick_event
fig.canvas.mpl_connect('pick_event', on_pick)

# Habilitar a capacidade de seleção
ax.set_picker(True)

# Exibir a figura
plt.show()
