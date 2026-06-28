import torch
import torch.nn as nn
import numpy as np

class AsymmetricPsiTNeuron(nn.Module):
    def __init__(self, in_features, out_features):
        super().__init__()
        self.weights = nn.Parameter(torch.randn(out_features, in_features, dtype=torch.complex64) * 0.8)
        self.bias = nn.Parameter(torch.zeros(out_features, dtype=torch.complex64))
        self.alpha = nn.Parameter(torch.ones(out_features) * 1.5)
        self.beta = nn.Parameter(torch.zeros(out_features))
        self.gamma = nn.Parameter(torch.ones(out_features) * 2.0)

    def forward(self, x):
        z = torch.matmul(x, self.weights.t()) + self.bias
        R = torch.abs(z)
        theta = torch.angle(z)
        amplitude = torch.tanh(R)
        angle_asym = torch.relu(theta + self.beta)
        phi_att = np.pi * self.gamma * torch.tanh(self.alpha * R) * torch.sin(angle_asym)
        return amplitude * torch.complex(torch.cos(phi_att), torch.sin(phi_att))
