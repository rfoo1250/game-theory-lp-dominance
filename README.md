# Mixed Strategy Dominance via MILP

A Python script that uses Gurobi to detect pure strategies dominated by mixed strategies in normal-form games. This tool performs Iterated Elimination of Dominated Strategies (IEDS) using MILP.  {placeholder} To perform Iterated Elimination of Dominated Strategies (IEDS), particularly identifying when a pure strategy is dominated by a mixed strategy—a more nuanced form of dominance often ignored in basic IEDS.

## Features

- MILP formulation to detect mixed dominance
- Iterative elimination of dominated strategies
- Gurobi-powered optimization
- Easily extensible for different matrix sizes

## Requirements

- Python 3.8+
- Gurobi Optimizer with `gurobipy`
- NumPy
