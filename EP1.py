#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 11:27:18 2024

@author: jessechoi
"""
#Jesse Choi 
### this file contians linear algebra with numpy on bond pricing


import pandas as pd
import numpy as np

def bond_price(times, cashflows, rate):
    """
    calculates and returns the price of a bond, given it’s series of cashflows and discount rate. 
    """
    values = [1/(1+rate)**times[i] * (cashflows[i]) for i in range(len(times))]
    
    return sum(values)


def bootstrap(cashflows, prices):
    """parameters cashflows, which is a matrix (2-dimensional list) containing 
    the cashflows for some bonds, and prices which is a column matrix 
    (2-dimensional list) containing the prices of these bonds.
    """
    cashflow_inv = np.linalg.inv(np.matrix(cashflows))
    
    return cashflow_inv @ np.matrix(prices).T

def bond_duration(times, cashflows, rate):
    """calculate and return the duration metric for a bond. 
    The parameters are: times is a list of the times at which the cashflows occur;
    cashflows is a list of the cashflows for this bond;
    r is the periodic (not annual) discount rate.
    """
    price = bond_price(times, cashflows, rate)
    disc_cashflows = [cashflows[i]/(1+rate)**(i+1) for i in range(len(times))]
    weights = [disc_cashflows[i]/price for i in range(len(times))]
    
    return np.dot(weights, times)




























