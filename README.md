# Cost of Living in Singapore Data Visualisation Analysis

This project explores the real vs perceived cost of living in Singapore, analysing the effects of taxes, healthcare costs, and essential living expenses across different income groups. We compare Singapore's situation with other countries and evaluate the impact of government interventions from 2014 to present.

Our analysis focuses on four key domains: 
- **Taxes**: GST, income tax, and property tax
- **Healthcare**: Affordability of healthcare services and products
- **Necessities**: Costs of food, transport, and utilities 
- **Global Comparison**: Benchmarking Singapore against other countries

The target audiences include researchers, policymakers, and informed citizens interested in understanding Singapore's evolving economic landscape.

---
## Getting Started

We use [`uv`](https://docs.astral.sh/uv/) as our Python dependency manager. You may be able to ru nthe notebooks with Anaconda, but using `uv` is **strongly recommended** to ensure consistent environment.

### Prerequisites

Install `uv` (requires Python 3.8+). You can install it using:
```bash
pip install uv
```

### Setup Instructions 
Clone this repository and run: 
```bash
uv sync 
```
This will install all dependencies defined in `pyproject.toml`.

---
## Running the Notebooks
To explore the data processing and visualisation steps:
```bash
uv run jupyter-lab
```
This opens Jupyter Lab in your browser. You can then run each notebook in sequence to reproduce our charts and findings.

## Launching the Dashboard
To view the interactive dashboard for this project: 
```bash
uv run dashboard
```
This will start the visual dashboard we developed to showcase the data insights in a dynamic, user-friendly interface.

## Repository Structure
```bash
.
├── dashboard           # Source code for visual dashboard
├── devenv.lock
├── devenv.nix
├── devenv.yaml
├── packages            # Notebooks and scripts for data processing and linking to dashboard
├── pyproject.toml
├── README.md
└── uv.lock
```

## Project Summary 
Through this analysis, we aim to: 
- Compare perceived vs actual costs in Singapore 
- Evaluate government policies like tax reliefs and subsidies
- Benchmark affordability against international standards
- Support informed dialogue and policy decisions with data-driven insights

