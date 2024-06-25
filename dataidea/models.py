# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/Python-Data-Analysis/Week4-ML-Intro/41_overview_of_machine_learning.ipynb.

# %% auto 0
__all__ = ['loadModel', 'saveModel']

# %% ../nbs/Python-Data-Analysis/Week4-ML-Intro/41_overview_of_machine_learning.ipynb 61
import joblib

def loadModel(filename='model.di'):
    """
    Load a model from a file using joblib.

    Parameters:
    filename (str): The path to the file containing the model.

    Returns:
    object: The loaded model.
    """
    return joblib.load(filename)

def saveModel(model, filename='model.di'):
    """
    Save a model to a file using joblib.

    Parameters:
    model (object): The model to be saved.
    filename (str): The path to the file where the model will be saved.

    Returns:
    None
    """
    joblib.dump(model, filename)
