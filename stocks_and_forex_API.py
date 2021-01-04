from finnhub import client as Finnhub
import pandas as pd
import datetime

client = Finnhub.Client(api_key="burenjf48v6u5d1lc1cg") #public key
normalize_flag = True
divide_by_max_flag = False
start = int(datetime.datetime(2017,12,1).timestamp())
end = int(datetime.datetime(2020,12,31).timestamp())
resolution = "W" # 1, 5, 15, 30, 60, D, W, M
value_type = "h" # c v h l

def normalize(numbers):
    maximum = max(numbers)
    minimum = min(numbers)
    return [(x-minimum)/(maximum-minimum) for x in numbers]
    
def divide_by_max(numbers):
    maximum = max(numbers)
    return [x/maximum for x in numbers]

def plot_finnhub_data(symbol, finnhub_data, value_type):
    if normalize_flag:
        finnhub_data[value_type] = normalize(finnhub_data[value_type])
    
    if divide_by_max_flag:
        finnhub_data[value_type] = divide_by_max(finnhub_data[value_type])
    
    finnhub_data_ts = [datetime.datetime.fromtimestamp(x) for x in finnhub_data["t"]]
    finnhub_data_s = pd.Series(data=finnhub_data[value_type], index=finnhub_data_ts)

    finnhub_data_s.plot(label=symbol + " " + value_type, legend=True, grid=True)

def plot_stock(symbol, value_type=value_type):
    plot_finnhub_data(symbol, client.stock_candles(symbol, resolution, start, end), value_type)
 
def plot_crypto(symbol, value_type=value_type):
    plot_finnhub_data(symbol, client.crypto_candles(symbol, resolution, start, end), value_type)

def plot_forex(symbol, value_type=value_type):
    plot_finnhub_data(symbol, client.forex_candles(symbol, resolution, start, end), value_type)

# examples 


#Airlines
# plot_stock("LUV") 
# plot_stock("JETS")

#Oil
# plot_stock("XOM") # EXXON MOBIL CORP
# plot_stock("SHLX") # SHELL MIDSTREAM PARTNERS LP
# plot_stock("IXC") # ISHARES GLOBAL ENERGY ETF
# plot_stock("XLE") # "ENERGY SELECT SECTOR SPDR

#CocaCola 
# plot_stock("COKE")

#Carbon
# plot_stock("SMOG")

#Silver
# plot_stock("SIL")
# plot_stock("PSLV")
    
#Gold
# plot_stock("GDXJ")
    
#Pallad
# plot_stock("PALL")

#Pharma
# plot_stock("PLXP")
# plot_stock("PPH")
# plot_stock("PRTK")
# plot_stock("RARE")
# plot_stock("RCKT")

# FOREX
# plot_forex("OANDA:EUR_PLN")
# plot_forex("OANDA:USD_PLN")

# technology
# plot_stock("AAPL")
# plot_stock("TSLA")
# plot_stock("NIO")
# plot_stock("PLUG")


