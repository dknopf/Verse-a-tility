import numpy as np

def mahalonobis(x,data):
"""
Calculates the Mahalonobis distance from the average values
"""

    x_minus_mu = x- np.mean(data)
    cov = np.cov(data)

    
