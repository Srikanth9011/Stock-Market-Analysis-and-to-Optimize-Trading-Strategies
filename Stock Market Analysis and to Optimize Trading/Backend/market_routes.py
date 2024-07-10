from flask import jsonify
from server import app
import yfinance as yf
import locale

Nifty50 = ['ADANIENT.NS','ADANIPORTS.NS']

def Fetch_stock_data_Name(tickers):
    locale.setlocale(locale.LC_ALL, '')
    stock_data = []
    stocks = yf.Tickers(' '.join(tickers))
    for stock in tickers:
        try: 

            data = stocks.tickers[stock].info
            close = data['currentPrice']
            relevant_data = {
                'Name': data['shortName'],
                'Symbol': stock,
                'Close': close
            }
            stock_data.append(relevant_data)  # Convert to dictionary
        except Exception as e:
            print(f"Error fetching data for {stock}: {e}")
    return stock_data


def categorize_stocks():

    Index = ['^NSEI', '^BSESN', '^NSEBANK']
    Box_index=Fetch_stock_data_Name(Index[:6])
    return {
        'index_data': Box_index[:3], #
        'chart_table': Box_index
    }



@app.route('/dashboard3')
def get_dashboard3():
    stock_data = categorize_stocks()
    return jsonify(stock_data)