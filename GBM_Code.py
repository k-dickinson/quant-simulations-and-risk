import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf


ticker = yf.Ticker("SPY")
latest = ticker.history(period="1d")

# Get just the latest close price
latest_close = latest['Close'].iloc[-1]


S0 = latest_close        # starting stock price
mu = 0.10       # expected annual return
sigma = 0.1123   # annual volatility
T = 1           # time in years
N = 252         # number of steps
dt = T / N      # time step size

Z = np.random.normal(0, 1, N)

S = np.zeros(N)
S[0] = S0
for t in range(1, N):
    S[t] = S[t-1] * np.exp((mu - 0.5 * sigma**2)*dt + sigma*np.sqrt(dt)*Z[t])

plt.plot(S)
plt.title("Simulated Stock Price Using GBM")
plt.xlabel("Day")
plt.ylabel("Price")
plt.show()