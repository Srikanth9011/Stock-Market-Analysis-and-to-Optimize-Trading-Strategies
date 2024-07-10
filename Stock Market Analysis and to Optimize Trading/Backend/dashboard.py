from flask import jsonify
from server import app
import yfinance as yf
import locale

Nifty50 = ['APOLLOHOSP.NS','ASIANPAINT.NS','AXISBANK.NS','BAJAJ-AUTO.NS','BAJFINANCE.NS','BAJAJFINSV.NS','BPCL.NS','BHARTIARTL.NS','BRITANNIA.NS','CIPLA.NS','COALINDIA.NS','DIVISLAB.NS','DRREDDY.NS','GRASIM.NS','HCLTECH.NS','HDFCLIFE.NS','HEROMOTOCO.NS','HINDALCO.NS','ITC.NS','HDFCBANK.NS','ICICIBANK.NS','SBIN.NS','KOTAKBANK.NS','INDUSINDBK.NS','ADANIENT.NS','ADANIPORTS.NS','EICHERMOT.NS','HINDUNILVR.NS','INFY.NS','JSWSTEEL.NS','LTIM.NS','LT.NS','M&M.NS','MARUTI.NS','NTPC.NS','NESTLEIND.NS','ONGC.NS','POWERGRID.NS','RELIANCE.NS','SBILIFE.NS','SHRIRAMFIN.NS','SUNPHARMA.NS','TCS.NS','TATACONSUM.NS','TATAMOTORS.NS','TATASTEEL.NS','TECHM.NS','TITAN.NS','ULTRACEMCO.NS','WIPRO.NS']
# #Nifty50_Names = ['HDFC Bank','ICICI Bank','Axis Bank','State Bank of India','Kotak Mahindra Bank','IndusInd Bank','Adani Enterprises', 'Adani Ports', 'Apollo Hospitals', 'Asian Paints',  'Bajaj Auto', 'Bajaj Finance', 'Bajaj Finserv', 'Bharat Petroleum', 'Bharti Airtel', 'Britannia Industries', 'Cipla', 'Coal India', "Divi's Laboratories", "Dr. Reddy's Laboratories", 'Eicher Motors', 'Grasim Industries', 'HCL Technologies', 'HDFC Life Insurance Company', 'Hero MotoCorp', 'Hindalco Industries', 'Hindustan Unilever', 'ITC', 'Infosys', 'JSW Steel', 'LTIMindtree', 'Larsen & Toubro', 'Mahindra', 'Maruti Suzuki', 'NTPC', 'Nestle India', 'Oil & Natural Gas', 'Power Grid', 'Reliance Industries', 'SBI LIC', 'Shriram Finance', 'Sun Pharmaceutical', 'Tata Consultancy Services', 'Tata Consumer Products', 'Tata Motors', 'Tata Steel', 'Tech Mahindra', 'Titan Company', 'UltraTech Cement', 'Wipro']
# nifty_rem=['HDFCBANK.NS','ICICIBANK.NS','AXISBANK.NS','SBIN.NS','KOTAKBANK.NS','INDUSINDBK.NS']
# Bank_rem=['BANKBARODA.NS','PNB.NS','FEDERALBNK.NS','IDFCFIRSTB.NS','AUBANK','BANDHANBNK']
Index = ['^NSEI', '^BSESN', '^NSEBANK','^CNXIT','NIFTY_FIN_SERVICE.NS','^CNXENERGY','^CNXMETAL','^CNXFMCG','^CNXAUTO']
Index_Names = ['NIFTY50', 'SENSEX', 'BANK-NIFTY','NIFTY-IT','NIFTY-FINANCE','NIFTY-ENERGY','NIFTY-METAL','NIFTY-FMCG','NIFTYAUTO']
nifty_weight={"ITC.NS":3.03,"HINDUNILVR.NS":2.67,"BAJAJFINSV.NS":1.20,"LT.NS":2.74,"RELIANCE.NS":12.86,"SUNPHARMA.NS":1.34,"MARUTI.NS":1.37,"TITAN.NS":1.37,"TATASTEEL.NS":1.37,"TECHM.NS":1.05,"POWERGRID.NS":1.04,"M&M.NS":1.18,"TATAMOTORS.NS":1.05,"NTPC.NS":0.99,"HINDALCO.NS":0.94,"ONGC.NS":0.78,"WIPRO.NS":1.01,"ULTRACEMCO.NS":1.02,"GRASIM.NS":0.85,"INDUSINDBK.NS":0.85,"ADANIPORTS.NS":0.82,"JSWSTEEL.NS":0.94,"DIVISLAB.NS":0.77,"NESTLEIND.NS":0.87,"CIPLA.NS":0.68,"TATACONSUM.NS":0.66,"BAJAJ-AUTO.NS":0.65,"DRREDDY.NS":0.67,"SBILIFE.NS":0.65,"HCLTECH.NS":1.53,"COALINDIA.NS":0.51,"APOLLOHOSP.NS":0.61,"HDFCLIFE.NS":0.72,"UPL.NS":0.60,"TCS.NS":4.91,"BRITANNIA.NS":0.52,"KOTAKBANK.NS":3.51,"HEROMOTOCO.NS":0.43,"INFY.NS":7.66,"SHREECEM.NS":0.46,"ICICIBANK.NS":6.90,"SBIN.NS":2.54,"AXISBANK.NS":2.57,"BHARTIARTL.NS":2.33,"BAJFINANCE.NS":2.37,"ASIANPAINT.NS":1.95,"BPCL.NS":0.46,"HDFCBANK.NS":8.10,"EICHERMOT.NS":0.49}

#get the stock data high,close,open with id as 1,2,3 for dashboard
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
                'symbol':stock,
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
#fetching data for index ones
def Fetch_stock_data_Name(stocks, stock_names):
    stock_data = []
    bargraph={}
    locale.setlocale(locale.LC_ALL, '')  # Set the locale to the user's default
    for stock, stock_name in zip(stocks, stock_names):
        try:
            ticker = yf.Ticker(stock)
            data = ticker.history(period="5d", interval='1d')  # Fetch daily data 
            
            latest_data = data.iloc[-1]  # Get the latest data point

            close = latest_data['Close']
            close_pre = data['Close'][-2]
            percent=((close-close_pre)/close_pre)*100
            bargraph[stocks]=percent

            relevant_data = {
                'Name': stock_name,
                'Close': close,
                'change': close-close_pre,
                'high':latest_data['High'],
                'low':latest_data['Low'],
                'percent': percent
            }
            stock_data.append(relevant_data)  # Convert to dictionary
        except Exception as e:
            print(f"Error fetching data for {stock}: {e}")
    return stock_data ,bargraph

#dashboard chart data 
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

#merge all the data for dashboard
def categorize_stocks(sorted_stocks,Box_index):

    # chart_symbol_ind= ['^NSEI', '^BSESN', '^NSEBANK','^CNXIT','NIFTY_MID_SELECT.NS','NIFTY_FIN_SERVICE.NS']
    # chart_name_ind=['NIFTY','SENSEX','BANK-NIFTY','NIFTY-IT','SENSEX-MID','NIFTY-FINANCE']
    # index_data = chart_index_data(chart_symbol_ind,chart_name_ind)

    #Box_index=Fetch_stock_data_Name(Index[:6],Index_Names[:6])
    top_gainers = sorted_stocks[:7]  # Top 5 gainers
    top_losers = sorted_stocks[-7:][::-1]  # Top 5 losers
    return {
        'index_data': Box_index[:4],
        'chart_table': Box_index,
        # 'chart_data' : index_data,
        'top_gainers': top_gainers,
        'top_losers': top_losers,
        'heat_map': sorted_stocks

    }

nifty50_data=Fetch_stock_data(Nifty50) #nifty50 data or all stocks
sorted_nifty50 = sorted(nifty50_data, key=lambda x: x['percent'],reverse=True) #all nifty50 sorted by percentage data or all stocks

Box_index,dash_barchart=Fetch_stock_data_Name(Index,Index_Names)

dashboard_data = categorize_stocks(sorted_nifty50,Box_index[:6]) #all the dashboard data except bar table

@app.route('/dashboard')
def dashboard():
    return jsonify(dashboard_data)
#only for dashbard bar
@app.route('/barchart')
def barchart():
    return jsonify(dash_barchart)



@app.route('/gainlose')
def gain_lose():
    return jsonify(nifty50_data)

 #to store barchart in index contribution
def contribution(index_value_previous,niftyweight,niftydata):
    positive_contribution = []
    negative_contribution = []
    contributions_dict = {}
    pos_val=0
    neg_val=0
    # Calculate contributions and categorize them
    for data in niftydata:
        stock_name = data['symbol']
        if stock_name in niftyweight:
            weight = niftyweight[stock_name]
            close = data['Close']
            percent_change = data['percent']
            contribution = (index_value_previous * weight * percent_change) / 10000
            contributions_dict[stock_name] = contribution
            if contribution >= 0:
                pos_val=pos_val+contribution
                positive_contribution.append({'Name': stock_name,'close':close,'change':percent_change,'Contribution': contribution})
            else:
                neg_val=neg_val+contribution
                negative_contribution.append({'Name': stock_name,'close':close,'change':percent_change, 'Contribution': contribution})

    # Print the datasets
    sorted_positive_contribution = sorted(positive_contribution, key=lambda x: x['change'], reverse=True)

    # Sort negative contribution dataset
    sorted_negative_contribution = sorted(negative_contribution, key=lambda x: x['change'])
    return {
        'gain':sorted_positive_contribution,
        'lose':sorted_negative_contribution,
        'gain_val':pos_val,
        'neg_val':neg_val},contributions_dict

index_contri,contri_bar=contribution(22000,nifty_weight,nifty50_data)

@app.route('/index_contribution')
def index_cont():
    return jsonify(index_contri)

@app.route('/barstock')
def index_contri_bar():
    return jsonify(contri_bar)

