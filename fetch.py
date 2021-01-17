## PYTHON EXTENSIONS NECESSARY

#%%
import yfinance as yf
import datetime
import pandas as pd
import matplotlib.pyplot as plt
#%%
stock = 'PLTR'

#%%
#stockdata = yf.download(stock)
#print(type(stockdata))
#print(stockdata.Close)
#print(stockdata.tail())
#stockdata.head()
#stockdata.info

#%%

today = datetime.date.today()
before_days = today - datetime.timedelta(2*365)

str(before_days)
str(today)
#%%


stockticker = yf.Ticker(stock)
stockhistory = stockticker.history(start=before_days, end=today)

# %%

def getMovingAverage(data, t):
    df = data
    mvg_avg = data['Close'].rolling(window=t).mean()
    colname = 'Moving Avg ' + str(t)
    df[colname] = mvg_avg
    return df


df = stockhistory[['Close']]
#close_history

#df = getMovingAverage(df, 20)

df = getMovingAverage(df, 38)
df = getMovingAverage(df, 50)
df = getMovingAverage(df, 100)
df = getMovingAverage(df, 200)
 


    



# %%
viewed = df.tail(50)
viewed.plot()

# %%

# plt.plot(last_fifity['Close'])

# %%
# compare 2 Plots:
data = yf.download('SPY AAPL')
data.tail()

data.tail(30)['Close'].plot(figsize=(10, 5))

# %%
