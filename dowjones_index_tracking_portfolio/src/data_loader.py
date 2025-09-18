path_to_data = r"C:\Users\amosa\Documents\My Graduate School\FALL 2025\Courses\AMS 518_Advanced Stochastic Models, Risk Assessment, and Portfolio Optimization\Assignments\Assignment 2\Assignment Resources"

dow_index_close_prices = pd.read_csv(os.path.join(path_to_data, 'dow_index_close_prices.csv')).set_index("Date")
dow_index_daily_log_returns = pd.read_csv(os.path.join(path_to_data, 'dow_index_daily_log_returns.csv')).set_index("Date")
stocks_50_close_prices = pd.read_csv(os.path.join(path_to_data, 'stocks_50_close_prices.csv')).set_index("Date")
stocks_50_daily_log_returns = pd.read_csv(os.path.join(path_to_data, 'stocks_50_daily_log_returns.csv')).set_index("Date")