#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 17:19:55 2024

@author: jessechoi
"""
# Jesse Choi 
# This file contains the plots

import matplotlib.pyplot as plt
import numpy as np
import datetime as dt

from EP2 import *

def plot_stock_prices(symbols):
    """which creates a graph of the historical stock prices for several stocks. 
    This function should take a parameter which is a list of stock symbols. 
    For each stock symbol, the function will expect a .csv file containing 
    stock price data (i.e., from Yahoo Finance), with monthly stock prices, 
    for example the data files above.
    """
    df = get_stock_prices_from_csv_files(symbols)

    plt.title("stock prices")
    plt.xlabel('Date')
    plt.ylabel('Price')
    
    for symbol in symbols: #plotting each stock
        plt.plot(df.index, df[f"{symbol}"])
    
    plt.legend(symbols)

    plt.show();
    
def plot_stock_cumulative_change(symbols):
    """which creates a graph of the cumulative stock returns for several stock.
    This function should take a parameter which is a list of stock symbols. 
    For each stock symbol, the function will expect a .csv file containing 
    stock price data (i.e., from Yahoo Finance), with monthly stock prices, 
    for example the data files above.
    """
    
    df = get_stock_prices_from_csv_files(symbols)

    cumulative_change = pd.DataFrame(index=df.index, columns=df.columns)
    
    for column in df.columns: #iterating through columns
        cumulative_change[column] = df[column] / df.iloc[0][column]
    
    plt.title("stock prices")
    plt.xlabel('Date')
    plt.ylabel('Price')
    
    for symbol in symbols: #plotting each stock
        plt.plot(cumulative_change.index, cumulative_change[f"{symbol}"])
    
    plt.legend(symbols)

    plt.show();
    
def plot_efficient_frontier(symbols):
    """to create a graph of the efficient frontier (the set of minimum variance 
    portfolios) that can be achieved using a small set of assets.
    """
    
    returns =  get_stock_returns_from_csv_files(symbols) #calculted returns and covariance from stocks
    covar = get_covariance_matrix(returns)
    
    #converting to matrices
    v = np.matrix(covar)
    e = np.matrix(returns.mean())
    w = calc_global_min_variance_portfolio(v) #Finding portfolio with lowest variance
    
    global_min_returns = calc_portfolio_return(e, w) #finding the return of that portfolio
    
    global_min_stdev = calc_portfolio_stdev(v, w) # finding the stdev of that portfolio
    
    rs = np.linspace(global_min_returns - global_min_stdev, global_min_returns + global_min_stdev) #made a range of 1 standard deviation

    
    x = calc_efficient_portfolios_stdev(e, v, rs) 

    
    y = rs
    
    #Plotting
    plt.title("Efficient Frontier")
    plt.xlabel("Portfolio Standard Deviation")
    plt.ylabel("Portfolio Expected Return")
    plt.plot(x, y) 
        
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    