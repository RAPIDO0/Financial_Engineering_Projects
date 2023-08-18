#Implementing Black-Scholes formula
#https://fr.wikipedia.org/wiki/Mod%C3%A8le_Black-Scholes#:~:text=le%20mod%C3%A8le%20Black%2DScholes%20ou,stochastique%20en%20temps%20discret%20(cf.
import numpy as np
from scipy.stats import norm

#definig variable
r = 0.01    #interest rate
S = 30      #price of the underlying asset
K = 40      #strike price
T = 240/365     #time of option expiration
sigma = 0.30    #volatility

def blackScholes(r, S, K, T, sigma, type="C"):
    #Calculate the BlackScholes option price for a call/put
    d1 = 1/(sigma*np.sqrt(T)) * (np.log(S/K) + (r + 0.5*sigma**2)*T)
    d2 = d1 - sigma*np.sqrt(T)
    
    try:
        if type == "C":
            price = S*norm.cdf(d1, 0, 1) - K*np.exp(-r*T)*norm.cdf(d2, 0, 1)
        elif type == "P":
            price = -S*norm.cdf(-d1, 0, 1) + K*np.exp(-r*T)*norm.cdf(-d2, 0, 1)
        return price
    except:
        print("wrong parameter enter")


print("CALL Option Price is: ", round(blackScholes(r, S, K, T, sigma, type="C"), 2))            
print("PUT Option Price is: ", round(blackScholes(r, S, K, T, sigma, type="P"), 2))            