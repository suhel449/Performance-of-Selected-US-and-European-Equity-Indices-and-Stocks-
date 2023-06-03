#!/usr/bin/env python
# coding: utf-8

# In[8]:


import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# 

# 

# In[23]:


# Define the stock symbol and time period
symbol = 'AAPL,GSK.L'
start_date = '2018-01-01'
end_date = '2022-12-31'


# 

# In[24]:


# Fetch historical stock data
stock_data = yf.download(symbol, start=start_date, end=end_date)


# In[25]:


# Calculate daily returns
stock_data['Returns'] = stock_data['Close'].pct_change()


# 

# 

# In[26]:


# Calculate moving averages
stock_data['MA50'] = stock_data['Close'].rolling(window=50).mean()
stock_data['MA200'] = stock_data['Close'].rolling(window=200).mean()


# In[27]:


# Plot the stock price and moving averages
plt.figure(figsize=(10, 6))
plt.plot(stock_data['Close'], label='Stock Price')
plt.plot(stock_data['MA50'], label='50-day Moving Average')
plt.plot(stock_data['MA200'], label='200-day Moving Average')
plt.title(symbol + ' Stock Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()


# In[28]:


# Load historical price data into a pandas DataFrame
data = pd.read_csv('historical_data.csv')


# In[29]:


# Calculate the daily returns
data['Returns'] = data['Close'].pct_change()


# In[18]:


# Calculate the volatility
volatility = np.sqrt(252) * data['Returns'].std()  # Assuming 252 trading days in a year

print('Volatility:', volatility)


# In[ ]:




