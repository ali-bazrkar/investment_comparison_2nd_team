import yfinance as yf
import pandas as pd
import matplotlib.plot as plt

# Define the tickers for each asset
tickers = {
    'Oil': 'CL=F',            # Crude Oil WTI
    'Gold': 'GC=F',           # Gold Futures
    'Dollar Index': 'DX-Y.NYB',  # US Dollar Index
    'Bitcoin': 'BTC-USD'      # Bitcoin USD
}

# Create an empty dictionary to store dataframes
dataframes = {}

# Set the start and end dates
start_date = '2015-01-01'
end_date = '2024-01-01'

# Download the data for each asset
for asset, ticker in tickers.items():
    data = yf.download(ticker, start=start_date, end=end_date)
    data['Asset'] = asset
    dataframes[asset] = data[['Close']].rename(columns={'Close': f'{asset} Price'})

# Merge the dataframes on Date
merged_data = pd.concat(dataframes.values(), axis=1, join='inner')

# Save the merged data to a CSV file
merged_data.to_csv('merged_asset_prices.csv')

# Show a preview of the data
#print(merged_data.head())

data = pd.read_csv("merged_asset_prices.csv")
data.head()

data.info()
print(data.describe())

# Set the plot size
plt.figure(figsize=(14, 8))

# Plot the price for each asset
for asset in tickers.keys():
    plt.plot(merged_data.index, merged_data[f'{asset} Price'], label=asset)

# Add titles and labels
plt.title('Asset Prices (2015-2024)', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Price (USD)', fontsize=12)

# Add a legend
plt.legend()

# Show the plot
plt.show()



