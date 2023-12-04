import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import argparse
import os
import yfinance as yf

def scrape_monthly_data(ticker):
    nov_15 = datetime(datetime.now().year, 11, 15)
    url = f'https://finance.yahoo.com/quote/{ticker}/history?period1=0&period2={int(nov_15.timestamp())}&interval=1mo&filter=history&frequency=1mo'

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

def fetch_financial_statements(ticker_symbol):
    # Create a Ticker object
    ticker = yf.Ticker(ticker_symbol)

    # Fetch financial statements
    financial_statements = {
        'annual_income_statement': ticker.financials.T,
        #'quarterly_income_statement': ticker.quarterly_financials.T,
        'annual_balance_sheet': ticker.balance_sheet.T,
        #'quarterly_balance_sheet': ticker.quarterly_balance_sheet.T,
        'annual_cash_flow': ticker.cashflow.T,
        #'quarterly_cash_flow': ticker.quarterly_cashflow.T
    }
    ticker = ticker_symbol
    # Save the data to csv files
    folder_path = '../data/raw'
    annual_income_statement_file_name = f'{ticker}_annual_income_statement.csv'
    annual_balance_sheet_file_name = f'{ticker}_annual_balance_sheet.csv'
    annual_cash_flow_file_name = f'{ticker}_annual_cash_flow.csv'
    annual_income_statement_file_path = os.path.join(folder_path, annual_income_statement_file_name)
    annual_balance_sheet_file_path = os.path.join(folder_path, annual_balance_sheet_file_name)
    annual_cash_flow_file_path = os.path.join(folder_path, annual_cash_flow_file_name)
    # Check if the file already exists
    if os.path.isfile(annual_income_statement_file_path) or os.path.isfile(annual_balance_sheet_file_path) or os.path.isfile(annual_cash_flow_file_path):
        print(f"The financial files already exist.")
    else:
        df_annual_income_statement = pd.DataFrame(financial_statements['annual_income_statement'])
        df_annual_balance_sheet = pd.DataFrame(financial_statements['annual_balance_sheet'])
        df_annual_cash_flow = pd.DataFrame(financial_statements['annual_cash_flow'])
        df_annual_income_statement.to_csv(annual_income_statement_file_path, index=True)
        df_annual_balance_sheet.to_csv(annual_balance_sheet_file_path, index=True)
        df_annual_cash_flow.to_csv(annual_cash_flow_file_path, index=True)
        #df.to_csv(csv_file_path, index=False)
        print(f"The financial files has been created.")
    return financial_statements


def main():
    parser = argparse.ArgumentParser(description='scrape monthly data from Yahoo Finance website')
    parser.add_argument('ticker', type=str, help='ticker of stock')

    args = parser.parse_args()
    monthly_data = scrape_monthly_data(args.ticker)
    financial_data = fetch_financial_statements(args.ticker)
    print("This is the first 5 rows of data we scraped:\n", monthly_data[:5])
    print(f"This is the annual income statement data of {args.ticker}\n", financial_data['annual_income_statement'])
    
if __name__ == "__main__":
    main()
