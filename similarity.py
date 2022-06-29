import numpy as np


def similarity(patch1, patch2):
    # Pearson Distance
    diff = (patch1.astype(np.double) - patch2.astype(np.double)) * (patch1.astype(np.double) - patch2.astype(np.double))
    diff = diff / patch2.astype(np.double)

    sim = np.sum(diff)
    sim = np.exp(-(sim / 10))

    return sim
