# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 19:44:38 2020

@author: Hageresebb
"""
import cvxpy as cp
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(40)
y = 0.3 * x + 5 + np.random.standard_normal(40)
plt.scatter(x, y)

def estimate_coef(x, y): 
    # number of observations/points 
    n = np.size(x) 
  
    # mean of x and y vector 
    m_x, m_y = np.mean(x), np.mean(y) 
  
    # calculating cross-deviation and deviation about x 
    SS_xy = np.sum(y*x) - n*m_y*m_x 
    SS_xx = np.sum(x*x) - n*m_x*m_x 
  
    # calculating regression coefficients 
    b_1 = SS_xy / SS_xx 
    b_0 = m_y - b_1*m_x 
  
    return(b_0, b_1) 
  
def plot_regression_line(x, y, b): 
    # plotting the actual points as scatter plot 
    plt.scatter(x, y, color = "m", 
               marker = "o", s = 30) 
  
    # predicted response vector 
    y_pred = b[0] + b[1]*x 
  
    # plotting the regression line 
    plt.plot(x, y_pred, color = "g") 
  
    # putting labels 
    plt.xlabel('x') 
    plt.ylabel('y') 
  
    # function to show plot 
    plt.show() 
def plot_regression_with_CVXY():
    b0 = cp.Variable()
    b1 = cp.Variable()
    obj = 0
    for i in range(40):
        obj += (b0 * x[i] + b1 - y[i]) ** 2
    cp.Problem(cp.Minimize(obj), []).solve()
    b0 = b0.value; b1 = b1.value
    plt.scatter(x, y)
    plt.plot(x, b0 * x + b1)
  
def main(): 
    # observations 

    # estimating coefficients 
    b = estimate_coef(x, y) 
    
    print("Estimated coefficients:\nb_0 = {}  \ nb_1 = {}".format(b[0], b[1])) 
  
    # plotting regression line 
    plot_regression_line(x, y, b) 
    plot_regression_with_CVXY()
  
if __name__ == "__main__": 
    main() 
    # calculating regression coefficients 
    b_1 = SS_xy / SS_xx 
    b_0 = m_y - b_1*m_x 
  
    return(b_0, b_1) 
  
def plot_regression_line(x, y, b): 
    # plotting the actual points as scatter plot 
    plt.scatter(x, y, color = "m", 
               marker = "o", s = 30) 
  
    # predicted response vector 
    y_pred = b[0] + b[1]*x 
  
    # plotting the regression line 
    plt.plot(x, y_pred, color = "g") 
  
    # putting labels 
    plt.xlabel('x') 
    plt.ylabel('y') 
  
    # function to show plot 
    plt.show() 
def plot_regression_with_CVXY():
    b0 = cp.Variable()
    b1 = cp.Variable()
    obj = 0
    for i in range(40):
        obj += (b0 * x[i] + b1 - y[i]) ** 2
    cp.Problem(cp.Minimize(obj), []).solve()
    b0 = b0.value; b1 = b1.value
    plt.scatter(x, y)
    plt.plot(x, b0 * x + b1)
  
def main(): 
    # observations 

    # estimating coefficients 
    b = estimate_coef(x, y) 
    
    print("Estimated coefficients:\nb_0 = {}  \ nb_1 = {}".format(b[0], b[1])) 
  
    # plotting regression line 
    plot_regression_line(x, y, b) 
    plot_regression_with_CVXY()
  
if __name__ == "__main__": 
    main() 
