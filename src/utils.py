"""
Utility functions and classes extracted from the project notebook.

Notes:
- This file was generated automatically from `notebook/Final_Report.ipynb`.
- You can import from here in your notebook with: `from src.utils import *` (or specific names).
- Feel free to reorganize into multiple modules (e.g., data_utils.py, plot_utils.py) as the project grows.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels
import statsmodels.api as sm
import pandas_datareader.data as web
import matplotlib.ticker as mtick
from pandas_datareader.famafrench import get_available_datasets
import getFamaFrenchFactors as gff
import os
import time


from pathlib import Path
import pandas as _pd

def load_data(path: str | None = None):
    """
    Load the monthly dataset as a pandas DataFrame.

    Parameters
    ----------
    path : str | None
        Optional custom path to the CSV. If None, defaults to "data/monthly.csv"
        resolved relative to the project root.

    Returns
    -------
    pandas.DataFrame
    """
    if path is None:
        # Resolve relative to repository root even when running from notebook/
        root = Path(__file__).resolve().parents[1]
        path = root / "data" / "monthly.csv"
    else:
        path = Path(path)
    return _pd.read_csv(path)


# ===== Extracted from notebook cells =====

def performance_evaluation(returns):
    mean = returns.mean() 
    std = returns.std() 
    sharpe_ratio = mean / std
    skewness = returns.skew() 
    kurtosis = returns.kurtosis() + 3 

    cumulative_returns = (1 + returns).cumprod() - 1
    high_water_mark = cumulative_returns.cummax()
    drawdown = 1 - (cumulative_returns+1) / (high_water_mark+1)
    max_drawdown = drawdown.max()

    return sharpe_ratio, max_drawdown, skewness, kurtosis, cumulative_returns


def transaction_amount(weights, prices_shift1):
    return ((weights / prices_shift1).diff(1).abs() * prices_shift1).sum(axis="columns", skipna=False).fillna(1)

training_px_df = stock_price.shift(1).loc[training_portfolio_weights.index]
test_px_df = stock_price.shift(1).loc[test_portfolio_weights.index]

cost_coefficients = np.array([5, 10, 25, 50])/10000
performance_df = pd.DataFrame(index=cost_coefficients, dtype=float,
                              columns=["train_sharpe_ratio", "train_max_drawdown", "train_skewness", "train_kurtosis", 
                                       "test_sharpe_ratio", "test_max_drawdown", "test_skewness", "test_kurtosis"])
for cost_coefficient in cost_coefficients:

    training_return_with_transaction_cost = training_portfolio_returns - cost_coefficient * transaction_amount(training_portfolio_weights, training_px_df)
    training_sharpe_ratio, training_max_drawdown, training_skewness, training_kurtosis, training_cumulative_performance = performance_evaluation(training_return_with_transaction_cost)
    training_sharpe_ratio *= np.sqrt(252)

    test_return_with_transaction_cost = test_portfolio_returns - cost_coefficient * transaction_amount(test_portfolio_weights, test_px_df)
    test_sharpe_ratio, test_max_drawdown, test_skewness, test_kurtosis, test_cumulative_performance = performance_evaluation(test_return_with_transaction_cost)
    test_sharpe_ratio *= np.sqrt(252)
    
    performance_df.loc[cost_coefficient, :] = training_sharpe_ratio, training_max_drawdown, training_skewness, training_kurtosis, test_sharpe_ratio, test_max_drawdown, test_skewness, test_kurtosis
    

    fig, axes = plt.subplots(2, 1, figsize=(8, 6))

    ax = axes[0]
    training_cumulative_returns.plot(ax=ax, label="Before Transaction Costs")
    training_cumulative_performance.plot(ax=ax, label="After Transaction Costs")
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(1))
    ax.legend()
    ax.set_title(f"Training performance with {int(cost_coefficient*10000)} bp transaction cost", fontsize=12)
    ax.set_xlabel("")
    

    ax = axes[1]
    test_cumulative_returns.plot(ax=ax, label="Before Transaction Costs")
    test_cumulative_performance.plot(ax=ax, label="After Transaction Costs")
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(1))
    ax.legend()
    ax.set_title(f"Test performance with {int(cost_coefficient*10000)} bp transaction cost", fontsize=12)
    ax.set_xlabel("")
    fig.tight_layout()
    plt.show()
