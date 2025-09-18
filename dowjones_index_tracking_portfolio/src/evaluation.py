# PSG solved optimal positions in tracking
opt_positions = pos_df['Position'].to_numpy()

# Log return of assets (before rebalancing: all 50 stocks)
log_ret_mat = stocks_50_daily_log_returns.astype(float).to_numpy()
cum_log_ret = np.cumsum(log_ret_mat, axis=0)                    # sum from i=1 to i=50 of log_returns
cum_simple_returns = np.exp(cum_log_ret) - 1.0                  # SimpleCumReturn = e^{CumLogRet} - 1

# Value of each position and portfolio value at time t:
## V_{i,t} = position_{i}*(1+SimpleCumRet_{i,t}) = position_{i}*e^{CumLogRet}
pos_values_over_time = cum_simple_returns * opt_positions + opt_positions
## V_{t} = sum_{i=1}^{i=50} V_{i,t}
portfolio_value = pos_values_over_time.sum(axis=1)
## Scaled portfolio value to start at 100: Scaled V = 100* V_{t} / V_{0}
portfolio_value_scaled = 100.0 * portfolio_value / portfolio_value[0]

# Similarly, for the benchmark index
# Log return of ^GJI
index_log_ret = dow_index_daily_log_returns['^DJI'].astype(float).to_numpy()
## Cumulative log for ^GJI = sum_{s=1}^{t} ^GJI log returns for 1<= s<= t <=T
index_cum = np.cumsum(index_log_ret.astype(float))
## ^GJI index value scaled to start from 100: I_{t} = 100*e^{IndexCumLogRet_{t} - IndexCumLogRet_{0}}
index_value = np.exp(index_cum)
index_value_scaled = 100 * index_value / index_value[0]

# Time series of Scaled Replicating Portfolio and Scaled Benchmark Index
portfolio_series = pd.Series(portfolio_value_scaled, index = stocks_50_daily_log_returns.index, name='Replicating_Portfolio')
index_series = pd.Series(index_value_scaled, index = stocks_50_daily_log_returns.index, name='DJI')  