import requests

# Uncomment this and add your own key for the pset:
KEY = "92WZD9LFYAZ71HTV"


# Call this with your API url to yget your data from the service
# You don't have to add anything to this.
def make_api_call(url):
    """
    Makes a request to a url endpoint that responds in json and returns
    the result as a python data structure (a list or dictionary).
    This is a very optimistic function and doesn't check for errors.
    """
    return requests.get(url).json()


# Build your api url here. See
# https://www.alphavantage.co/documentation/#dailyadj
# do decide what values to add for the parameters.
def build_url(symbol):
    url = "https://www.alphavantage.co/query?"
    url += "function=TIME_SERIES_DAILY"
    url += f"&symbol={symbol}"
    url += f"&apikey={KEY}"
    return url


# Use this API url with your key and symbol
def get_quotes(symbol):
    """
    Takes a stock symbol and returns a list of tuples with the date
    and closing price for the last hundred days, for example,
    [ ('2022-07-15', '256.7200'), ('2021-07-15', '254.0800'), ... ]
    """
    res = make_api_call(build_url(symbol))
    if "Error Message" in res:
        print("Error:", res["Error Message"])
        exit(1)
    return [(k, float(v["4. close"])) for k, v in res["Time Series (Daily)"].items()]


def main():
    # print out the date and price table described in the pset.
    symbol = input("Enter symbol: ")
    data = get_quotes(symbol)
    print(f"Last hundred days price data for {symbol}:")
    for date, price in data:
        print(date, f"${price:.2f}")


if __name__ == "__main__":
    main()
