import matplotlib.pyplot as plt
from math import sqrt


def plot_blobs(blobs):
    ax = plt.gca()
    for blob in blobs:
        y, x, r = blob
        r = sqrt(2) * r
        c = plt.Circle((x, y), r, color='red', linewidth=2, fill=False)
        ax.add_patch(c)
