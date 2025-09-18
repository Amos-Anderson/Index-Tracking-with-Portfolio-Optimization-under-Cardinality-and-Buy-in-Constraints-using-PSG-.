initial_budget = 100
gamma = 0.06

normalized_stocks_50_daily_log_returns = stocks_50_daily_log_returns / (initial_budget*(1 - gamma))

combined_df = normalized_stocks_50_daily_log_returns.copy()

combined_df['scenario_benchmark'] = dow_index_daily_log_returns

headers = combined_df.columns.tolist()
track_port_matrix_body = np.column_stack([combined_df[str(h)].to_numpy() for h in headers])
track_port_matrix = [headers, track_port_matrix_body]