#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 15:11:08 2024

@author: jessechoi
"""

#Jesse Choi 
# this file contains functions about the efficient frontier 

import numpy as np
import pandas as pd

def calc_portfolio_return(e, w):
    """calculates and returns the portfolio return (as a float) for a 
        portfolio of n >= 2 assets. The parameters are:
        e is a matrix of expected returns for the assets
        w is a matrix of portfolio weights of the assets, which sums to 1."""
            
    return np.ravel(np.dot(e, w.T))[0]

def calc_portfolio_stdev(v, w): 
    """that calculates and returns the portfolio standard deviation 
    (as a float) for a portfolio of n >= 2 assets. The parameters are:
        v is a matrix of covariances among the assets, and
        w is a matrix of portfolio weights of the assets, which sums to 1.
    """
    return np.ravel(np.sqrt(w @ v @ w.T))[0]

def calc_global_min_variance_portfolio(v): 
    """that returns the portfolio weights corresponding to the global minimum 
    variance portfolio. That is, this function will find the portfolio with 
    the absolute minimum variance that can be composed of the selected assets,
    where v is the matrix of covariances among the assets.
    """
    c = ([1] * len(v)) @ np.linalg.inv(v) @ np.matrix([1] * len(v)).T
    variance = np.ravel(1/c)[0]
    w_p = ([variance]*len(v)) @ np.linalg.inv(v)
    
    return w_p

def calc_min_variance_portfolio(e, v, r): 
    """that finds and returns the portfolio weights corresponding to the minimum variance portfolio for the required rate of return r.
        The parameters are:
        e is a matrix of expected returns for the assets
        v is a matrix of covariances among the assets.
        r is the required rate of return
    """
    one = np.array([1] * len(v))
    a = np.ravel(one @ np.linalg.inv(v) @ e.T)[0]
    b = np.ravel(e @ np.linalg.inv(v) @ e.T)[0]
    c = np.ravel(one @ np.linalg.inv(v) @ one.T)[0]
    
    A = [[b,a],[a,c]]
    d = np.linalg.det(A)
        
    g = np.dot(1/d, np.subtract(np.dot(b, one), np.dot(a, e))) @ np.linalg.inv(v)
    
    h = np.dot(1/d, np.subtract(np.dot(c, e), np.dot(a, one))) @ np.linalg.inv(v)
    
    w_p = np.add(g, np.dot(h, r))
    
    return w_p

def calc_efficient_portfolios_stdev(e, v, rs):
    """which finds a series of minimum variance portfolios and returns their standard deviations.
        The parameters are: e is a matrix (1 x N) of expected returns for the assets
        v is a matrix (N x N) of covariances among the assets.
        rs is a numpy.array (1 x N) of rates of return for which to calculate 
        the corresponding minimum variance portfolio’s standard deviation
    """
    stdevs = np.array([])
    
    for r in rs:
        w = np.ravel(calc_min_variance_portfolio(e, v, r))
        sigma = calc_portfolio_stdev(v, w)  
        
        print(f"r = {r:.4f}, sigma = {sigma:.4f} w = {w}")
        stdevs = np.append(stdevs, sigma)   
        
    return stdevs

def get_stock_prices_from_csv_files(symbols):
    """to obtain a pandas.DataFrame containing historical stock prices for 
    several stocks. The parameter symbols will be a list of stock symbols, 
    and the return value will be a pandas.DataFrame containing the monthly 
    stock prices for each of those stock symbols, for the period of dates 
    given in the CSV files."""
    
    # for each stock symbol, create the appropriate file name to read:
        
    prices = pd.DataFrame()    
    for symbol in symbols: #Adding each stock as a column to the new df
        
        fn = f"{symbol}.csv"
        table = pd.read_csv(fn)
        table.index = pd.to_datetime(table['Date'])
        
        prices[symbol] = table["Adj Close"]

    return prices

def get_stock_returns_from_csv_files(symbols):
    """which will return a single pandas.DataFrame object containing the 
    stock returns. Begin by calling your function get_stock_prices_from_csv_files(symbols) 
    to obtain stock prices. Manipulate the data frame to convert from stock 
    prices into stock returns. The result of this function is to return a 
    single pandas.DataFrame object containing the stock returns.
    """
    prices = get_stock_prices_from_csv_files(symbols) 
    returns = prices / prices.shift(1) - 1
    
    return returns 

def get_covariance_matrix(returns):
    """which generates a covariance matrix for the stock returns in returns. 
    The parameter return will be a pandas.DataFrame object, i.e., the same 
    type as from the get_stock_returns_from_csv_files(symbols) function above.
    """
    return returns.cov()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    