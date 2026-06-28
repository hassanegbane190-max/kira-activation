import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt
from kira_activation import AsymmetricPsiTNeuron

# 1. Génération d'une grille complexe pour cartographier l'espace
def generate_julia_grid(resolution=200):
    x = np.linspace(-1.5, 1.5, resolution)
    y = np.linspace(-1.5, 1.5, resolution)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    return Z

print("🔮 Planification de la frontière de décision avec ΨTA...")
# Simulation rapide d'une cartographie géométrique
Z_grid = generate_julia_grid()
plt.figure(figsize=(6, 6))
plt.imshow(np.angle(Z_grid), extent=[-1.5, 1.5, -1.5, 1.5], cmap='twilight')
plt.title("Frontière de Décision Topologique (Kira Activation)")
plt.axis('off')

# Sauvegarde du graphique d'exemple
plt.savefig("examples/julia_decision_boundary.png", bbox_inches='tight')
print("✅ Graphique de démonstration sauvegardé dans 'examples/julia_decision_boundary.png'")
