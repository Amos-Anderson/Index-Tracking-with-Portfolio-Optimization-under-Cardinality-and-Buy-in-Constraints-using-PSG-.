# Optimal ouput
result['output']

# Optimal allocations
result['point_problem_1']

pos_df = pd.DataFrame({
    'Ticker': headers[:len(result['point_problem_1'][1])-1], 
    'Position': np.array(result['point_problem_1'][1][:-1], dtype=float)
})

# Which tickers were selected (non-zero)
selected = pos_df[pos_df.Position != 0].copy()
print("\nSelected tickers (non-zero):")
print(selected)

# Sort by position for quick inspection
pos_df_sorted = pos_df.reindex(pos_df.Position.abs().sort_values(ascending=False).index)