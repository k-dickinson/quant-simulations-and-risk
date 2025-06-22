import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

# Number of assets
n_assets = 3

# List of tickers
tickers = ["AAPL", "TSLA", "NVDA"]

def stock_pricing(symbol):
    ticker = yf.Ticker(symbol)
    latest = ticker.history(period="1d")
    return latest['Close'].iloc[-1]

# Get real starting prices dynamically
S0 = np.array([stock_pricing(t) for t in tickers])

# Time setup
T = 1  # 1 year
N = 252  # trading days
dt = T / N

# Portfolio weights (sum to 1)
weights = np.array([0.4, 0.3, 0.3])

# Annual drift and volatility
mu = np.array([0.08, 0.12, 0.10])
sigma = np.array([0.15, 0.20, 0.18])

# Correlation matrix
corr_matrix = np.array([
    [1.0, 0.2, 0.4],
    [0.2, 1.0, 0.3],
    [0.4, 0.3, 1.0]
])

cov_matrix = np.outer(sigma, sigma) * corr_matrix
L = np.linalg.cholesky(cov_matrix)

M = 10000  # simulations

# Initialize price paths
price_paths = np.zeros((M, N + 1, n_assets))
price_paths[:, 0, :] = S0

# Simulate GBM with correlated shocks
for m in range(M):
    Z = np.random.normal(size=(N, n_assets))
    correlated_Z = Z @ L.T
    for t in range(1, N + 1):
        price_paths[m, t, :] = price_paths[m, t - 1, :] * np.exp(
            (mu - 0.5 * sigma**2) * dt + np.sqrt(dt) * correlated_Z[t - 1]
        )

# Compute weighted portfolio value per simulation & timestep
portfolio_values = np.sum(price_paths * weights, axis=2)  # shape (M, N+1)

# Scale portfolio so initial value = 100,000
initial_portfolio_value = np.sum(S0 * weights)
scale_factor = 100000 / initial_portfolio_value
portfolio_values *= scale_factor

# Plotting side by side
fig, axs = plt.subplots(1, 2, figsize=(16, 6))

# ---- Left plot: Simulation paths ----
for i in range(10000):
    axs[0].plot(portfolio_values[i])
axs[0].set_title("Sample Simulated Portfolio Paths")
axs[0].set_xlabel("Time Step (Day)")
axs[0].set_ylabel("Portfolio Value ($)")
axs[0].grid(True)

# Add portfolio weights and starting prices as text box
weights_percent = weights * 100
textstr = '\n'.join((
    "Portfolio Weights & Starting Prices:",
    *(f"{tickers[i]}: {weights_percent[i]:.1f}% @ ${S0[i]:.2f}" for i in range(n_assets))
))
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
axs[0].text(0.05, 0.95, textstr, transform=axs[0].transAxes, fontsize=10,
            verticalalignment='top', bbox=props)

# ---- Right plot: Histogram of final portfolio values ----
final_values = portfolio_values[:, -1]
axs[1].hist(final_values, bins=50, edgecolor='black')
axs[1].set_title("Distribution of Final Portfolio Values")
axs[1].set_xlabel("Portfolio Value at T ($)")
axs[1].set_ylabel("Frequency")
axs[1].grid(True)

# Compute VaR at 95% confidence
VaR_95 = np.percentile(final_values, 5)

# Plot VaR vertical line
axs[1].axvline(VaR_95, color='r', linestyle='--', label=f'VaR (5%): ${VaR_95:,.0f}')

# Calculate % chance portfolio ends below initial 100k (loss)
pct_loss = np.mean(final_values < 100000) * 100
axs[1].axvline(100000, color='orange', linestyle='--', label='Initial Portfolio Value')
axs[1].legend()

# Add text box for VaR and loss %
textstr2 = f"Value at Risk (5% quantile): ${VaR_95:,.2f}\n" \
           f"Chance of Loss (below $100k): {pct_loss:.2f}%"
# Add text box for VaR and loss % in top right, just above legend
axs[1].text(0.95, 0.95, textstr2, transform=axs[1].transAxes, fontsize=10,
            verticalalignment='top', horizontalalignment='right',
            bbox=props)


plt.tight_layout()
plt.show()
