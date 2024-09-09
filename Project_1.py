import yfinance as yf
import pandas as pd

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
print(merged_data.head())

data = pd.DataFrame("merged_asset_prices.csv")
data.head()
