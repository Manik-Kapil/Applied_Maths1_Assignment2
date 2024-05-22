import numpy as np

def rmse(predictions, targets):
    """
    Calculate the Root Mean Square Error between predictions and targets.
    """
    pred = np.array(predictions)
    tar = np.array(targets)
    rmse = np.sqrt(np.mean((pred - tar) ** 2))
    return rmse