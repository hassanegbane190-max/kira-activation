# 🚀 Kira Activation: Asymmetric Psi-Transcendence (ΨTA)

Kira Activation is a groundbreaking complex-valued neural network activation layer designed to master chaotic, highly non-linear, and fractal topologies natively in the complex plane C.

## 📊 Performance Benchmark

Tested against state-of-the-art **GELU** activation on the highly chaotic **Julia Fractal Dataset**:
- **GELU Accuracy:** 85.89%
- **ΨTA Accuracy:** **99.83%** 🌟

## 💻 Quick Start

```python
from kira_activation import AsymmetricPsiTNeuron
import torch

layer = AsymmetricPsiTNeuron(in_features=1, out_features=8)
x = torch.tensor([[0.5 + 0.5j]], dtype=torch.complex64)
output = layer(x)
print(output)
```
