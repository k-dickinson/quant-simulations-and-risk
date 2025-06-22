# Stock Price Simulation and Risk Analysis in Python

---

Hi, I’m Kyle — an incoming math student at Carnegie Mellon University, documenting my journey into quantitative finance. This project explores how mathematical models can simulate stock price behavior, assess portfolio performance, and measure financial risk. It begins with Geometric Brownian Motion (GBM) to model individual stock paths, expands into Monte Carlo simulations across thousands of scenarios, and culminates in a portfolio-level risk analysis using correlation structures, and metrics like Value at Risk (VaR) and probability of loss. Along the way, it demonstrates techniques used in real-world quantitative research and trading.

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

This forms the base for more complex models like Monte Carlo simulations for portfolios, option pricing, or risk modeling, which are discussed later on.

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

You can check out the full simulation code [here](https://github.com/k-dickinson/geometric-brownian-motion/blob/main/GBM_Code.py)

---

## What is a Monte Carlo Simulation?

A Monte Carlo simulation models uncertainty by running the same process (like GBM) many times using random inputs. In finance, this helps us:

- Visualize a range of possible outcomes
- Estimate the probability of gains or losses
- Measure risk under extreme market conditions

Earlier, We simulate a single stock path — but the framework supports scaling to thousands of simulations and portfolio-level analysis which you can see below.

---

## Example Output

![Sample Monte Carlo Simulation Output](https://github.com/k-dickinson/quant-simulations-and-risk/blob/main/monte_carlo_example_output.png)
---

## How it works

Basic Parameters:

```python
S0 = 100          # initial stock price
mu = 0.1          # expected anunual return
sigma = 0.1123    # annual volatility
T = 1             # time in years
N = 252           # number of steps
dt = int(T/N)     # number of steps
M = 10000         # number of simulation paths
```

Simulation:
```python
# Set up matrix for all paths
price_paths = np.zeros((M, N+1))
price_paths[:, 0] = S0   # initialize all paths at S0

# Generate all random shocks (Z) at once
Z = np.random.normal(0, 1, size=(M, N))

# Simulate paths
for t in range(1, N+1):
    price_paths[:, t] = price_paths[:, t-1] * np.exp(
        (mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z[:, t-1]
    )
```

You can check out the full simulation code [here](https://github.com/k-dickinson/quant-simulations-and-risk/blob/main/Monte_Carlo_GBM.py)

---

## Visualizing Risk: Histogram + Path Plot

To analyze the risk in a meaningful way, we can:

- Plot multiple simulated price paths
- Create a histogram of the final prices across all simulations

This lets us estimate downside risk with:

- Value at Risk (VaR) – the worst expected loss at a confidence level
- Probability of Loss – the probability of the stock having returns below the value you entered at

Example side-by-side output:

![Sample Monte Carlo Simulation Output](https://github.com/k-dickinson/quant-simulations-and-risk/blob/main/Monte_Carlo_Outputs_Sidebyside.png)

---

## Monte Carlo Portfolio Simulation Using Matrix Multiplication

In this final section, we simulate a multi-asset portfolio using:

* Geometric Brownian Motion (GBM)
* Monte Carlo simulation (10,000 paths)
* Matrix multiplication to model correlated returns
* Risk metrics like Value at Risk (VaR) and probability of loss

This helps us estimate the range of possible portfolio outcomes more realistically than treating each asset as independent.

---

## Why Matrix Multiplication?

Assets like AAPL, TSLA, and NVDA often move together — meaning their returns are correlated. To simulate this properly:

1. Define a correlation matrix between assets
2. Compute the covariance matrix:

```python
cov_matrix = np.outer(sigma, sigma) * correlation_matrix
```

3. Apply Cholesky decomposition to get a lower-triangular matrix `L` such that:

```
cov_matrix ≈ L @ L.T
```

4. Generate standard normal random shocks `Z` (shape: time steps × assets), then create correlated shocks:

```python
correlated_Z = Z @ L.T
```

This gives us realistic joint behavior between the assets — if Tesla crashes, Nvidia may follow, and our model reflects that.

---

## How the Simulation Works

* Tickers: AAPL, TSLA, NVDA
* Weights: `[0.4, 0.3, 0.3]`
* Drift: annual expected returns `[8%, 12%, 10%]`
* Volatility: annualized `[15%, 20%, 18%]`
* Correlation matrix: manually specified
* Simulation horizon: 252 trading days
* Number of simulations: 10,000
* Portfolio value at start: \$100,000

At each timestep for each simulation, the asset prices evolve via GBM, and we compute the weighted portfolio value.

---

## Example Output

![Portfolio Simulation Output](https://github.com/k-dickinson/quant-simulations-and-risk/blob/main/Portfolio_MonteCarlo_Figure.png)

---

## Visualizing the Results

* **Left plot:** 10,000 simulated portfolio paths over time
* **Right plot:** Histogram of ending portfolio values

  * Red line = 95% Value at Risk (VaR)
  * Orange line = \$100,000 initial value
  * Text box = risk summary (VaR and % chance of loss)

---

## Why This Matters

This simulation gives a realistic view of potential future outcomes for a portfolio. It shows:

* How uncertainty grows over time
* How diversification helps reduce risk
* What extreme downside scenarios (VaR) might look like

---

## Skills Demonstrated

This model demonstrates:

* Stochastic modeling (GBM)
* Portfolio-level Monte Carlo simulation
* Correlated asset behavior via matrix decomposition
* Vectorized, production-style code
* Risk analysis (VaR, probability of loss)

These are highly relevant to quant research, trading, and strategist roles — especially at firms like SIG, IMC, Citadel, or smaller prop shops.

You can check out the full simulation code [here](https://github.com/k-dickinson/quant-simulations-and-risk/blob/main/portfolio_montecarlo_gbm.py)

---

## Related Videos

Check out my Instagram breakdown where I explain this parts of this model through analogies:
[Instagram Link](https://instagram.com/quant_kyle)

---

## Questions?

If you have any questions, feel free to drop them in the [Instagram](https://instagram.com/quant_kyle) comments or open an issue!

---

## Resources I Used

* [GBM Article: Quant Start](https://www.quantstart.com/articles/geometric-brownian-motion-simulation-with-python/?utm_source=chatgpt.com)
* [GBM Video: Dummy R](https://www.youtube.com/watch?app=desktop&v=5A2iNvpAv1w%5C)
* [Monte Carlo Video: MarbleScience](https://www.youtube.com/watch?v=7ESK5SaP-bc)
* [Monte Carlo Video: IBM Technology](https://www.youtube.com/watch?v=7TqhmX92P6U)
