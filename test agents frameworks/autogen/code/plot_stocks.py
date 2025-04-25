# filename: plot_stocks.py
import yfinance as yf
import matplotlib.pyplot as plt

# Define the stock symbols and the date range
tickers = ['META', 'TSLA']
start_date = '2020-01-01'
end_date = '2024-01-01'

# Download historical data
data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']

# Plotting the stock prices
plt.figure(figsize=(14, 7))
for ticker in tickers:
    plt.plot(data[ticker], label=ticker)

plt.title('Stock Prices of META and Tesla from 2020 to 2024')
plt.xlabel('Date')
plt.ylabel('Adjusted Close Price (USD)')
plt.legend()
plt.grid()
plt.show()