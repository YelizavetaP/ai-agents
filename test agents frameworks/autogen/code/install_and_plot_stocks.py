# filename: install_and_plot_stocks.py
import subprocess
import sys

# Helper function to install packages
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install necessary libraries
try:
    import yfinance as yf
except ImportError:
    install('yfinance')

try:
    import matplotlib.pyplot as plt
except ImportError:
    install('matplotlib')

# Now we can import yfinance and proceed with the plotting
import yfinance as yf
import matplotlib.pyplot as plt

# Define the stock symbols and the date range
tickers = ['META', 'TSLA']
start_date = '2020-01-01'
end_date = '2024-01-01'

# Download historical data
data = yf.download(tickers, start=start_date, end=end_date)

# Print the entire DataFrame and its columns for verification
print("DataFrame:")
print(data)
print("\nDataFrame columns:")
print(data.columns)

# Extract 'Close' prices using .loc
try:
    close_data = data['Close']
    
    # Print close data for diagnosis
    print("\nClose Price Data:")
    print(close_data)
    
    # Plotting the stock prices
    plt.figure(figsize=(14, 7))
    plt.plot(close_data['META'], label='META')
    plt.plot(close_data['TSLA'], label='TSLA')

    plt.title('Stock Prices of META and Tesla from 2020 to 2024')
    plt.xlabel('Date')
    plt.ylabel('Close Price (USD)')
    plt.legend()
    plt.grid()
    plt.show()
except KeyError as e:
    print(f"KeyError: {e}. Please check the printed DataFrame structure above.")