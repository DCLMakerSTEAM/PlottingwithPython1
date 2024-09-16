import requests
import matplotlib.pyplot as plt
import datetime
import time
import getpass

# Prompt for API key (hidden input)
api_key = getpass.getpass("Please enter your Finnhub API key: ")

# Finnhub API URL for quote
url = "https://finnhub.io/api/v1/quote"

# Function to fetch the current price of AAPL using the REST API
def fetch_stock_price():
    try:
        response = requests.get(url, params={'symbol': 'AAPL', 'token': api_key})
        data = response.json()
        return data['c']  # 'c' is the current price
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

# Setup plot
plt.ion()  # Enable interactive mode
fig, ax = plt.subplots()
prices = []
times = []

# Poll for stock prices in a loop
try:
    while True:
        current_price = fetch_stock_price()
        if current_price is not None:
            current_time = datetime.datetime.now()

            # Append to data lists
            times.append(current_time)
            prices.append(current_price)

            # Clear the axes and plot updated data
            ax.clear()
            ax.plot(times, prices, marker='o')

            # Set plot labels and title
            ax.set_title('AAPL Stock Price (Real-Time)')
            ax.set_xlabel('Time')
            ax.set_ylabel('Price (USD)')

            # Format time axis
            fig.autofmt_xdate()

            # Pause to update the plot
            plt.pause(1)

        # Wait for a few seconds before fetching the next price
        time.sleep(5)

except KeyboardInterrupt:
    print("\nPolling stopped.")

