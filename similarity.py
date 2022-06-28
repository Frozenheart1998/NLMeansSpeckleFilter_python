import numpy as np


def similarity(patch1, patch2):
    # Pearson Distance
    diff = (patch1 - patch2) * (patch1 - patch2)
    diff = diff / patch2

    sim = np.sum(diff)
    sim = np.exp(-(sim / 10))

    return sim
