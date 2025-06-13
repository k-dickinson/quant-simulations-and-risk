# geometric-brownian-motion
Simulating stock price paths using Geometric Brownian Motion (GBM) in Python

# Geometric Brownian Motion Simulation for Stock Prices

Hi, I’m Kyle — an incoming math student at Carnegie Mellon University, documenting my journey into quantitative finance. This project is part of a larger portfolio simulation I’m building, starting with the Geometric Brownian Motion model, a fundamental tool in quant finance.

---

## What is Geometric Brownian Motion?

GBM is a stochastic process widely used to model the behavior of stock prices over time. It assumes:

* Constant drift (average return)
* Constant volatility
* Log-normal distribution of prices

It’s a core assumption behind models like Black-Scholes, and a building block in Monte Carlo simulations.

---

## Model Equation

The GBM equation is:

$$
dS_t = \mu S_t dt + \sigma S_t dW_t
$$

Where:

* $S_t$: Stock price at time t
* $\mu$: Expected return (drift)
* $\sigma$: Volatility
* $W_t$: Wiener process (Brownian motion)

In discretized form:

$$
S_{t+1} = S_t \cdot \exp\left((\mu - \frac{1}{2} \sigma^2)\Delta t + \sigma \sqrt{\Delta t} \cdot Z_t\right)
$$

Where $Z_t \sim \mathcal{N}(0, 1)$

---

## What This Project Does

* Simulates a single or multiple GBM stock price paths
* Plots them over time
* Demonstrates how volatility and drift affect long-term outcomes

This forms the base for more complex models like Monte Carlo simulations for portfolios, option pricing, or risk modeling, which I'll be adding soon.

---

## Example Output

*(Insert a plot screenshot here — matplotlib or seaborn generated paths from your simulation)*

---

## How It Works (Python)

Basic parameters:

```python
S0 = 100          # initial stock price
mu = 0.1          # expected anunual return
sigma = 0.1123    # annual volatility
T = 1             # time in years
N = 252           # number of steps
dt = int(T/N)     # number of steps
```

Simulation:

```python
Z = np.random.normal(0, 1, N)
S = np.zeros(N)
S[0] = S0
for t in range(1, N):
    S[t] = S[t-1] * np.exp((mu - 0.5 * sigma**2)*dt + sigma*np.sqrt(dt)*Z[t])
```

---

## Related Video

Check out my Instagram breakdown where I explain this model visually:
[Instagram Link](https://instagram.com/quant_kyle)

---

## What’s Next

This is just phase 1 of my broader project. Upcoming improvements:

* Monte Carlo simulation with GBM
* Portfolio of assets with correlation
* Risk metrics (VaR, CVaR)

---

## Questions?

  If you have any questions, feel free to drop them in the [Instagram comments](https://instagram.com/quant_kyle) or open an issue!

---

## Resources I Used

* [GBM Article: Quant Start](https://www.quantstart.com/articles/geometric-brownian-motion-simulation-with-python/?utm_source=chatgpt.com)
* [GBM Youtube Video: Dummy R](https://m.youtube.com/watchv=5A2iNvpAv1w&pp=ygUZR2VvbWV0cmljIGJyb3duaWFuIG1vdGlvbg%3D%3D)
