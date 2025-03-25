"""
Main simulation logic for the carbon market SDE model.
"""

import numpy as np

def simulate_price_path(
    T=1.0, N=500, P0=1.0, alpha=0.5, delta=2.0, g0=0.4, lam=2.0,
    beta=0.3, sigma0=0.2, gamma=1.0, eta=0.1,
    theta=0.3, kappa=0.5, lambda0=10, seed=None
):
    if seed is not None:
        np.random.seed(seed)

    dt = T / N
    P = np.zeros(N+1)
    P[0] = P0
    time = np.linspace(0, T, N+1)

    for t in range(N):
        gt = g0 * np.exp(-lam * time[t])
        mu = alpha * (1 - P[t]**delta) + gt + beta * P[t] * gt
        dWt = np.random.normal(0, np.sqrt(dt))
        dNt = np.random.poisson(lambda0 * dt)
        sigma = sigma0 * (1 + gamma * np.sin(P[t])) + eta * P[t] * dNt
        J = theta * P[t]**(1 + kappa) * (1 + lam * gt) * dNt
        P[t+1] = P[t] + mu * dt + sigma * dWt + J

    return time, P
