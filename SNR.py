import numpy as np


def SNR(img1, noise):

    num = 0
    den = 0
    img1 = img1.astype(np.double)
    noise = noise.astype(np.double)
    for i in range(1, img1.shape[0] + 1):
        for j in range(1, img1.shape[1] + 1):
            num = num + (img1[i-1, j-1]**2 + noise[i-1, j-1]**2)
            den = den + (img1[i-1, j-1] - noise[i-1, j-1])**2
    print(num)
    print(den)
    loss = float(num) / (float(den) + 1e-13)
    loss = float(loss)
    loss = 10 * np.log10(loss)
    return loss
