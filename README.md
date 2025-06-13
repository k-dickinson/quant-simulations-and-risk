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

## How Geometric Brownian Motion Works

At its core, GBM assumes that stock prices grow continuously over time, but with some randomness. We use a formula that captures both the average growth (drift) and the randomness (volatility).

Here’s the equation we use to simulate it:

$$
S_{t+1} = S_t \cdot \exp\left((\mu - \frac{1}{2} \sigma^2)\Delta t + \sigma \sqrt{\Delta t} \cdot Z_t\right)
$$

Where:

* $S_t$: The stock price at time $t$
* $\mu$: The average return (drift)
* $\sigma$: The volatility (how much it varies)
* $\Delta t$: A small time step (like 1/252 for daily steps)
* $Z_t$: A random value drawn from a standard normal distribution (mean 0, standard deviation 1). Think of it like a weighted coin flip that can nudge the stock price up or down by a random amount, based on volatility.

This formula basically says: take the current price, and adjust it using both the average return and some randomness. That’s what gives the simulated path its wiggly, realistic shape.

It’s powerful because it captures the idea that while we can expect growth over time, prices also bounce around in unpredictable ways.


## What This Project Does

* Simulates a single or multiple GBM stock price paths
* Plots them over time
* Demonstrates how volatility and drift affect long-term outcomes

This forms the base for more complex models like Monte Carlo simulations for portfolios, option pricing, or risk modeling, which I'll be adding soon.

---

## Example Output

![Sample GBM Output](https://github.com/k-dickinson/geometric-brownian-motion/blob/main/GBM_Simulation.png)
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
You can check out the full simulation code [here](https://github.com/k-dickinson/geometric-brownian-motion/blob/main/GBM_Code.py).

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

  If you have any questions, feel free to drop them in the [Instagram](https://instagram.com/quant_kyle) comments or open an issue!

---

## Resources I Used

* [GBM Article: Quant Start](https://www.quantstart.com/articles/geometric-brownian-motion-simulation-with-python/?utm_source=chatgpt.com)
* [GBM Youtube Video: Dummy R](https://m.youtube.com/watchv=5A2iNvpAv1w&pp=ygUZR2VvbWV0cmljIGJyb3duaWFuIG1vdGlvbg%3D%3D)
