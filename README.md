# Index Tracking with Portfolio Optimization under Cardinality and Buy-in Constraints

## Objective
This project replicates the Dow Jones Industrial Average (^DJI) by constructing a tracking portfolio of up to 50 U.S. stocks, subject to **cardinality, buy-in, and budget constraints**.  
The optimization is solved using [Portfolio Safeguard (PSG)](https://uryasev.ams.stonybrook.edu/research/testproblems/financialengineering/case-study-portfolio-replication-with-cardinality-and-buyin-constraints/).

## Methodology
- Data: Historical close prices and daily log returns for the Dow Jones index and 50 candidate stocks.
- Optimization Problem:
  - **Objective:** Minimize maximum absolute tracking error.
  - **Constraints:**  
    - Cardinality: select at most *K* assets.  
    - Buy-in: minimum position size if selected.  
    - Budget + transaction cost constraints.
- Solver: PSG (with Python API). Please contact Professor Stan Uryasev for exclusive access to the use of PSG via `Stanislav.Uryasev@stonybrook.edu`.
- Verification: Compare the cumulative performance of the tracking portfolio with ^DJI, both scaled to start at 100.

## Repository Structure
- `data/` : Input CSV files (prices, log returns).  
- `src/` : Python scripts for data handling, optimization, and evaluation.  
- `notebooks/` : Jupyter notebook with full workflow (Assignment 1).  
- `results/` : Saved optimal positions, plots, and reports.

## Results
- Sparse tracking portfolio (~3 assets selected).  
- Portfolio vs Dow Jones performance plotted side by side.  
- Transaction cost and tracking error reported.
