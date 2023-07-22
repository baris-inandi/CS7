import json
import requests

# Uncomment this and add your own key for the pset:
# KEY =


# Call this with your API url to get your data from the service
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
    url += "function=???"
    url += "&symbol=???"
    url += "&apikey=???"    
    return url

# Use this API url with your key and symbol
def get_quotes(symbol):
    """
    Takes a stock symbol and returns a list of tuples with the date
    and closing price for the last hundred days, for example,
    [ ('2022-07-15', '256.7200'), ('2021-07-15', '254.0800'), ... ]
    """
    # Add your code here


def main():
    # Add your solution to the problem that makes use of the above to
    # print out the date and price table described in the pset.
    print("Remove me and add your code!")


if __name__ == "__main__":
    main()
