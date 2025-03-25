
# Carbon Market Simulation Project

This repository contains a simulation framework for modeling price dynamics in carbon emission trading markets using nonlinear stochastic differential equations (SDEs) with jump diffusion and policy feedback mechanisms.

## Features

- Simulates carbon price paths under policy and external shocks
- Models include:
  - Nonlinear drift with policy decay
  - Sinusoidal volatility feedback
  - Jump processes influenced by policy strength
- Visualizations:
  - Price path simulation
  - Final price distributions
  - Jump frequency and magnitude analysis
  - Parameter sensitivity heatmap

## Structure

- `/simulation/`: Python code modules
- `/output/`: Generated figures
- `/docs/`: Any documentation or write-ups
- `main_simulation.ipynb`: Jupyter notebook for full workflow
- `requirements.txt`: Python dependencies

## How to Run

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Open and run `main_simulation.ipynb` or use individual scripts in `/simulation/`

---

Developed by **Ziyuan Wang** (University of Toronto), 2025  
Submitted to **SIURO (SIAM Undergraduate Research Online)**
