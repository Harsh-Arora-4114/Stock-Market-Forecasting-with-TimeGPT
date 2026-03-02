import numpy as np
from scipy.optimize import minimize

def optimize_portfolio(returns):

    num_assets = returns.shape[1]
    mean_returns = returns.mean()
    cov_matrix = returns.cov()

    def portfolio_vol(weights):
        return np.sqrt(np.dot(weights.T,
                      np.dot(cov_matrix, weights)))

    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    bounds = tuple((0,1) for asset in range(num_assets))
    init_guess = num_assets * [1./num_assets]

    result = minimize(portfolio_vol,
                      init_guess,
                      method='SLSQP',
                      bounds=bounds,
                      constraints=constraints)

    return result.x