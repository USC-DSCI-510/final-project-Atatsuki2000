import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import argparse
import os

def scrape_monthly_data(ticker):
    # The URL format for the historical data page with a monthly interval
    url = f'https://finance.yahoo.com/quote/{ticker}/history?period1=0&period2={int(datetime.now().timestamp())}&interval=1mo&filter=history&frequency=1mo'

    # Send the GET request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    #response = requests.get(url)

    if response.status_code == 200:
      # Parse the HTML content
      soup = BeautifulSoup(response.content, 'html.parser')

      # The historical data is within a table with the 'data-test' attribute set to 'historical-prices'
      table = soup.find('table', attrs={'data-test': 'historical-prices'})

      # If the table is found, we'll iterate over its rows and pull out the data
      if table:
        headers = [header.text for header in table.findAll('th')]
        rows = []
        for row in table.findAll('tr'):
          # Get all columns in this row
          cols = row.findAll('td')
          if len(cols) == 7:  # Make sure we have the correct number of columns
            rows.append([data.text.strip() for data in cols])

        # Convert the data to a pandas DataFrame and return it
        df = pd.DataFrame(rows, columns=headers)
        folder_path = '../data/raw'
        csv_file_name = f'{ticker}_monthly.csv'
        csv_file_path = os.path.join(folder_path, csv_file_name)
        # Check if the file already exists
        if os.path.isfile(csv_file_path):
            print(f"The file '{csv_file_name}' already exists.")
        else:
            df.to_csv(csv_file_path, index=False)
            print(f"The file '{csv_file_name}' has been created.")
        return df
      else:
        print("Table not found on Yahoo Finance page")
        return None
    else:
      print('Failed to retrieve data')
      return None

def main():
    parser = argparse.ArgumentParser(description='scrape monthly data from Yahoo Finance website')
    parser.add_argument('ticker', type=str, help='ticker of stock')

    args = parser.parse_args()
    data = scrape_monthly_data(args.ticker)
    print("This is the first 5 rows of data:\n", data[:5])
    
if __name__ == "__main__":
    main()
