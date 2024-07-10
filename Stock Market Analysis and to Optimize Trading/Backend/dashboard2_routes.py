from flask import jsonify
from server import app
import yfinance as yf
import locale

# Nifty50 = ['ADANIENT.NS','ADANIPORTS.NS','APOLLOHOSP.NS','ASIANPAINT.NS','BAJAJ-AUTO.NS','BAJFINANCE.NS','BAJAJFINSV.NS','BPCL.NS','BHARTIARTL.NS','BRITANNIA.NS','CIPLA.NS','COALINDIA.NS','DIVISLAB.NS','DRREDDY.NS','EICHERMOT.NS','GRASIM.NS','HCLTECH.NS','HDFCLIFE.NS','HEROMOTOCO.NS','HINDALCO.NS','HINDUNILVR.NS','ITC.NS','INFY.NS','JSWSTEEL.NS','LTIM.NS','LT.NS','M&M.NS','MARUTI.NS','NTPC.NS','NESTLEIND.NS','ONGC.NS','POWERGRID.NS','RELIANCE.NS','SBILIFE.NS','SHRIRAMFIN.NS','SUNPHARMA.NS','TCS.NS','TATACONSUM.NS','TATAMOTORS.NS','TATASTEEL.NS','TECHM.NS','TITAN.NS','ULTRACEMCO.NS','WIPRO.NS']
# #Nifty50_Names = ['HDFC Bank','ICICI Bank','Axis Bank','State Bank of India','Kotak Mahindra Bank','IndusInd Bank','Adani Enterprises', 'Adani Ports', 'Apollo Hospitals', 'Asian Paints',  'Bajaj Auto', 'Bajaj Finance', 'Bajaj Finserv', 'Bharat Petroleum', 'Bharti Airtel', 'Britannia Industries', 'Cipla', 'Coal India', "Divi's Laboratories", "Dr. Reddy's Laboratories", 'Eicher Motors', 'Grasim Industries', 'HCL Technologies', 'HDFC Life Insurance Company', 'Hero MotoCorp', 'Hindalco Industries', 'Hindustan Unilever', 'ITC', 'Infosys', 'JSW Steel', 'LTIMindtree', 'Larsen & Toubro', 'Mahindra', 'Maruti Suzuki', 'NTPC', 'Nestle India', 'Oil & Natural Gas', 'Power Grid', 'Reliance Industries', 'SBI LIC', 'Shriram Finance', 'Sun Pharmaceutical', 'Tata Consultancy Services', 'Tata Consumer Products', 'Tata Motors', 'Tata Steel', 'Tech Mahindra', 'Titan Company', 'UltraTech Cement', 'Wipro']

# nifty_rem=['HDFCBANK.NS','ICICIBANK.NS','AXISBANK.NS','SBIN.NS','KOTAKBANK.NS','INDUSINDBK.NS']
# Bank_rem=['BANKBARODA.NS','PNB.NS','FEDERALBNK.NS','IDFCFIRSTB.NS','AUBANK','BANDHANBNK']

# Index = ['^NSEI', '^BSESN', '^NSEBANK','^CNXIT','NIFTY_FIN_SERVICE.NS','^CNXENERGY','^CNXMETAL','^CNXFMCG','^CNXAUTO']
# Index_Names = ['NIFTY50', 'SENSEX', 'BANK-NIFTY','NIFTY-IT','NIFTY-FINANCE','NIFTY-ENERGY','NIFTY-METAL','NIFTY-FMCG','NIFTYAUTO']


Nifty50 = ['ADANIENT.NS','ADANIPORTS.NS','APOLLOHOSP.NS','ASIANPAINT.NS','WIPRO.NS']
#Nifty50_Names = ['HDFC Bank','ICICI Bank','Axis Bank','State Bank of India','Kotak Mahindra Bank','IndusInd Bank','Adani Enterprises', 'Adani Ports', 'Apollo Hospitals', 'Asian Paints',  'Bajaj Auto', 'Bajaj Finance', 'Bajaj Finserv', 'Bharat Petroleum', 'Bharti Airtel', 'Britannia Industries', 'Cipla', 'Coal India', "Divi's Laboratories", "Dr. Reddy's Laboratories", 'Eicher Motors', 'Grasim Industries', 'HCL Technologies', 'HDFC Life Insurance Company', 'Hero MotoCorp', 'Hindalco Industries', 'Hindustan Unilever', 'ITC', 'Infosys', 'JSW Steel', 'LTIMindtree', 'Larsen & Toubro', 'Mahindra', 'Maruti Suzuki', 'NTPC', 'Nestle India', 'Oil & Natural Gas', 'Power Grid', 'Reliance Industries', 'SBI LIC', 'Shriram Finance', 'Sun Pharmaceutical', 'Tata Consultancy Services', 'Tata Consumer Products', 'Tata Motors', 'Tata Steel', 'Tech Mahindra', 'Titan Company', 'UltraTech Cement', 'Wipro']

nifty_rem=['HDFCBANK.NS','ICICIBANK.NS','AXISBANK.NS']
Bank_rem=['BANKBARODA.NS','PNB.NS','FEDERALBNK.NS']

Index = ['^NSEI', '^BSESN', '^NSEBANK','NIFTY_FIN_SERVICE.NS','^CNXIT','^CNXENERGY']
Index_Names = ['NIFTY50', 'SENSEX', 'BANK-NIFTY','NIFTY-FINANCE','NIFTY-IT','NIFTY-ENERGY']

#fetch all the stock data 
def Fetch_stock_data(tickers):
    locale.setlocale(locale.LC_ALL, '')
    stock_data = []
    stocks = yf.Tickers(' '.join(tickers))
    i=0
    for stock in tickers:
        try: 
            data = stocks.tickers[stock].info
            
            close = data['currentPrice']
            previous_close = data['previousClose']
            change = close - previous_close
            percent_change = (change / previous_close) * 100
            
            relevant_data = {
                'id':i+1,
                'Name': data['shortName'],
                'volume':data['volume'],
                'Close': close,
                'Open': data['open'],
                'High': data['dayHigh'],
                'Low': data['dayLow'],
                'change': change,
                'percent': percent_change,
                
            }
            i=i+1
            stock_data.append(relevant_data)  # Convert to dictionary
        except Exception as e:
            print(f"Error fetching data for {stock}: {e}")
        
    return stock_data
# fetch index data 
def Fetch_stock_data_Name(stocks, stock_names):
    stock_data = []
    locale.setlocale(locale.LC_ALL, '')  # Set the locale to the user's default
    for stock, stock_name in zip(stocks, stock_names):
        try:
            ticker = yf.Ticker(stock)
            data = ticker.history(period="2d", interval='1d')  # Fetch daily data
            latest_data = data.iloc[-1]  # Get the latest data point

            close = latest_data['Close']
            close_pre = data['Close'][-2]

            relevant_data = {
                'Name': stock_name,
                'Close': close,
                'change': close-close_pre,
                'high':latest_data['High'],
                'low':latest_data['Low'],
                'percent': ((close-close_pre)/close_pre)*100
            }
            stock_data.append(relevant_data)  # Convert to dictionary
        except Exception as e:
            print(f"Error fetching data for {stock}: {e}")
    return stock_data

def Bar_percent_sort(stocks, stock_names):
    percent_changes = {}
    locale.setlocale(locale.LC_ALL, '')  # Set the locale to the user's default
    for stock, stock_name in zip(stocks, stock_names):
        try:
            ticker = yf.Ticker(stock)
            data = ticker.history(period="2d", interval='1d')  # Fetch daily data
            close = data['Close'][-1]  # Today's close
            pre_close = data['Close'][-2] 

            percent_change = ((close -pre_close) / pre_close) * 100

            percent_changes[stock_name]=percent_change
        except Exception as e:
            print(f"Error fetching data for {stock}: {e}")
    return percent_changes

def chart_index_data(symbols, stock_names):
    data = {'time': []}
    for symbol, stock_name in zip(symbols, stock_names):
        # Fetch data from Yahoo Finance API
        stock_data = yf.download(symbol, period="1d", interval="15m")

        # Extract close prices and time
        close_prices = stock_data['Close'].round(0).astype(int).tolist()
        time = stock_data.index.strftime('%H:%M').tolist()

        # Add close prices to data
        data[stock_name] = close_prices

        # Add time to data if it's not already added
        if not data['time']:
            data['time'] = time

    return data

def categorize_stocks(sorted_stocks):
    # sorted_stocks = sorted(stock_data, key=lambda x: x['percent'],reverse=True)
    #needed name and chart data also
    # chart_symbol_ind= ['^NSEI', '^BSESN', '^NSEBANK','^CNXIT','NIFTY_MID_SELECT.NS','NIFTY_FIN_SERVICE.NS']
    # chart_name_ind=['NIFTY','SENSEX','BANK-NIFTY','NIFTY-IT','SENSEX-MID','NIFTY-FINANCE']
    # index_data = chart_index_data(chart_symbol_ind,chart_name_ind)
    Box_index=Fetch_stock_data_Name(Index[:6],Index_Names[:6])
    # index_data = chart_index_data(Index[:6],Index_Names[:6])

    #bar chart
    #Bar_chart = Bar_percent_sort(Index,Index_Names)

    top_gainers = sorted_stocks[:6]  # Top 5 gainers
    top_losers = sorted_stocks[-6:][::-1]  # Top 5 losers
    return {
        'index_data': Box_index[:4], 
        'chart_table': Box_index,
        # 'chart_data' : index_data,
        'top_gainers': top_gainers,
        'top_losers': top_losers,\
        'heat_map': sorted_stocks

    }


def contribution(index_value_previous,data_dict,data_list):
    positive_contribution = []
    negative_contribution = []
    contributions_dict = {}
    # Calculate contributions and categorize them
    for data in data_list:
        stock_name = data['Name']
        if stock_name in data_dict:
            weight = data_dict[stock_name]
            close = data['Close']
            percent_change = data['percent']
            contribution = (index_value_previous * weight * percent_change) / 100
            contributions_dict[stock_name] = contribution
            if contribution >= 0:
                positive_contribution.append({'Name': stock_name,'close':close,'change':percent_change,'Contribution': contribution})
            else:
                negative_contribution.append({'Name': stock_name,'close':close,'change':percent_change, 'Contribution': contribution})

    # Print the datasets
    sorted_positive_contribution = sorted(positive_contribution, key=lambda x: x['change'], reverse=True)

    # Sort negative contribution dataset
    sorted_negative_contribution = sorted(negative_contribution, key=lambda x: x['change'])

    # Print the sorted dataset


    return {
        'gain':sorted_positive_contribution,
        'lose':sorted_negative_contribution,
        'bar':contributions_dict
    }

nifty50_data=Fetch_stock_data(Nifty50)
nifty_rem_data=Fetch_stock_data(nifty_rem)
banknifty_data=Fetch_stock_data(Bank_rem)
#join all the index stock
nifty50_data=nifty50_data+nifty_rem_data
banknifty_data=nifty_rem_data+banknifty_data

#sort the index value on percent

sorted_stocks = sorted(nifty50_data, key=lambda x: x['percent'],reverse=True)
dashboard_data = categorize_stocks(sorted_stocks)

#chardata in dashboard


@app.route('/dashboard')
def dashboard2():
    return jsonify(dashboard_data)

@app.route('/gainlose')
def gainlose():
    return jsonify(sorted_stocks)



