# Proximal Policy Optimization (PPO) for Market Making

This repository provides an implementation of Proximal Policy Optimization (PPO) for automated market making on cryptocurrencies

## Overview

This repository provides an implementation of **Proximal Policy Optimization (PPO)** for automated market making using `quantpylib`, a proprietary library developed by HangukQuant. PPO, an advanced reinforcement learning algorithm, optimizes market making strategies by balancing exploration and exploitation, allowing for efficient, robust, and adaptive quoting strategies in financial markets.

**quantpylib** is a proprietary quantitative trading library developed by HangukQuant. To subscribe to HangukQuant's personal quant research, lectures, or access exclusive code libraries, please visit his [Substack page](https://hangukquant.substack.com).

## Features

- **PPO Algorithm**: Implements state-of-the-art reinforcement learning to dynamically optimize quoting strategies.
- **Market Making Strategy**: Adaptive inventory management and quote placement to maximize profitability and minimize risk.
- **Integration with quantpylib**: Utilizes quantpylib's proprietary infrastructure for seamless order management, execution, and data handling.
- **Backtesting and Simulation**: Easy-to-use framework to test and validate your strategies against historical market data.

## Installation

### Prerequisites

- Python 3.9+
- `quantpylib` (Proprietary - contact HangukQuant for access)

Install necessary dependencies:

```bash
pip install numpy pandas torch
```

##  Usage

To run the PPO market making strategy:

```bash
python ppo_market_maker.py
```

Ensure you have set up your API keys and configurations properly as instructed by `quantpylib` documentation.

## TODO: Performance Metrics

Key metrics tracked:
- Profit & Loss (P&L)
- Sharpe Ratio
- Maximum Drawdown
- Inventory Management Efficiency

##  Project Structure

```
PPO-Market-Making/
├── ppo_market_maker.py      # Main PPO algorithm
├── config.yaml              # Configuration parameters
├── README.md                # Documentation
└── .gitignore               # Files to ignore
```

##  License

This project is licensed under the **MIT License**.

##  Contributing

Contributions and improvements are welcome! Please open an issue or submit a pull request.

---

© 2025 HangukQuant. For more quant research, lectures, and access to exclusive code libraries, please subscribe to [HangukQuant's Substack](https://hangukquant.substack.com).


