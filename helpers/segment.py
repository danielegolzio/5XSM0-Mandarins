from skimage.segmentation import flood
from skimage.filters import gaussian, sobel, threshold_otsu, threshold_multiotsu
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
import numpy as np
import matplotlib.pyplot as plt

from .load import load
from .view import view


def segment_flood(image, tolerance):
    # image preprocessing
    image = (image - image.min()) / (image.max() - image.min())
    image = gaussian(image, sigma=5)
    edges = sobel(image)
    image = image * (1 - edges)

    points = []

    # get starting seeds from user
    def onclick(event):
        if event.button == 1:
            points.append((int(event.ydata), int(event.xdata)))

    fig, ax = plt.subplots()
    ax.imshow(image, cmap='gray')
    fig.canvas.mpl_connect('button_press_event', onclick)
    plt.title("Select seed points")
    plt.show()

    mask = np.zeros_like(image, dtype=bool)

    # create mask
    for point in points:
        mask = mask | flood(image, seed_point=point, tolerance=tolerance)

    plt.imshow(mask, cmap="gray")
    plt.title("Mask")
    plt.show()

    return mask


def segment_kmeans(image, K):
    # image preprocessing
    image = (image - image.min()) / (image.max() - image.min())
    image = gaussian(image, sigma=2)

    plt.imshow(image, cmap='gray')
    plt.title("Preprocessed Image")
    plt.show()

    # reshape image for clustering
    pixels = image.reshape(-1, 1)

    # k means clustering
    kmeans = KMeans(n_clusters=K, random_state=0).fit(pixels)
    clustered = kmeans.labels_.reshape(image.shape)

    plt.imshow(clustered, cmap='gray')
    plt.title("K-means Clustering")
    plt.show()

    return clustered

def segment_gmm(image, K):

    # image preprocessing
    image = (image - image.min()) / (image.max() - image.min())
    image = gaussian(image, sigma=2)

    plt.imshow(image, cmap='gray')
    plt.title("Preprocessed Image")
    plt.show()

    # reshape image for clustering
    pixels = image.reshape(-1, 1)

    # gmm clustering
    gmm = GaussianMixture(n_components=K, random_state=0).fit(pixels)
    clustered = gmm.predict(pixels).reshape(image.shape)

    plt.imshow(clustered, cmap='gray')
    plt.title("GMM Clustering")
    plt.show()

    return clustered


def segment_otsu(image):

    # image preprocessing
    image = (image - image.min()) / (image.max() - image.min())
    image = gaussian(image, sigma=2)

    plt.imshow(image, cmap='gray')
    plt.title("Preprocessed Image")
    plt.show()

    # threshold
    thresh = threshold_otsu(image)
    binary = image > thresh

    plt.imshow(binary, cmap='gray')
    plt.title("Otsu's Thresholding")
    plt.show()

    return binary


def segment_multiotsu(image, K):

    # image preprocessing
    image = (image - image.min()) / (image.max() - image.min())
    image = gaussian(image, sigma=2)

    plt.imshow(image, cmap='gray')
    plt.title("Preprocessed Image")
    plt.show()

    # multiclass threshold
    thresholds = threshold_multiotsu(image, classes=K)
    regions = np.digitize(image, bins=thresholds)

    plt.imshow(regions, cmap='gray')
    plt.title("Multi-Otsu's Thresholding")
    plt.show()

    return regions