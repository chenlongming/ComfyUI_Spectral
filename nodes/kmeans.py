from spectral import L2, L1
from spectral.io.bilfile import BilFile
from spectral.io.bipfile import BipFile
from spectral.io.bsqfile import BsqFile
from spectral.io.envi import SpectralLibrary
import torch
from matplotlib import pyplot as plt
from spectral.utilities.errors import NaNValueError
from tqdm.auto import tqdm

from ..utils.preprocess import image2tensor
import numpy as np


def kmeans_ndarray(image, n_clusters=10, max_iterations=20, **kwargs):
    if bool(np.isnan(image.min())):
        raise NaNValueError('Image data contains NaN values.')

    # defaults for kwargs
    start_clusters = None
    compare = None
    distance = L2
    iterations = None

    for (key, val) in list(kwargs.items()):
        if key == 'start_clusters':
            start_clusters = val
        elif key == 'compare':
            compare = val
        elif key == 'distance':
            if val in (L1, 'L1'):
                distance = L1
            elif val in (L2, 'L2'):
                distance = L2
            else:
                raise ValueError('Unrecognized keyword argument.')
        elif key == 'frames':
            if not hasattr(val, 'append'):
                raise TypeError('"frames" keyword argument must have "append"'
                                'attribute.')
            iterations = val
        else:
            raise NameError('Unsupported keyword argument.')

    nrows, ncols, nbands = image.shape
    N = nrows * ncols
    image = image.reshape((N, nbands))
    if start_clusters is not None:
        assert (start_clusters.shape[0] == n_clusters), 'There must be \
        nclusters clusters in the startCenters array.'
        centers = np.array(start_clusters)
    else:
        box_min = np.amin(image, 0)
        box_max = np.amax(image, 0)
        delta = (box_max - box_min) / (n_clusters - 1)
        centers = np.empty((n_clusters, nbands), np.float32)
        for i in range(n_clusters):
            centers[i] = box_min + i * delta

    distances = np.empty((N, n_clusters), np.float32)
    old_centers = np.array(centers)
    clusters = np.zeros((N,), np.int32)
    old_clusters = np.copy(clusters)
    diffs = np.empty_like(image, dtype=np.float32)
    itnum = 1
    t_bar = tqdm(total=max_iterations)
    while itnum <= max_iterations:
        try:
            # Assign all pixels
            for i in range(n_clusters):
                diffs = np.subtract(image, centers[i], out=diffs)
                if distance == L2:
                    distances[:, i] = np.einsum('ij,ij->i', diffs, diffs)
                else:
                    diffs = np.abs(diffs, out=diffs)
                    distances[:, i] = np.einsum('ij->i', diffs)
            clusters[:] = np.argmin(distances, 1)

            # Update cluster centers
            old_centers[:] = centers
            for i in range(n_clusters):
                inds = np.argwhere(clusters == i)[:, 0]
                if len(inds) > 0:
                    centers[i] = np.mean(image[inds], 0, np.float32)

            if iterations is not None:
                iterations.append(clusters.reshape(nrows, ncols))

            if compare and compare(old_clusters, clusters):
                break
            else:
                n_changed = np.sum(clusters != old_clusters)
                if n_changed == 0:
                    break

            old_clusters[:] = clusters
            old_centers[:] = centers
            itnum += 1
            t_bar.update()

        except KeyboardInterrupt:
            print("KeyboardInterrupt: Returning clusters from previous iteration.")
            return old_clusters.reshape(nrows, ncols), old_centers

    t_bar.close()

    return old_clusters.reshape(nrows, ncols), centers



class KMeans:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            'required': {
                'image': ('SPE',),
                'n_clusters': ('INT',),
                'max_iterations': ('INT', {'default': 20}),
            },
        }

    RETURN_TYPES = ('MASK', 'IMAGE', 'NDARRAY')
    RETURN_NAMES = ('classes mask', 'preview', 'clusters')

    CATEGORY = 'Spectral'
    FUNCTION = 'process'

    def process(self, image: BilFile | BipFile | BsqFile | SpectralLibrary, n_clusters: int, max_iterations: int = 20):
        samples = image.asarray()
        print(samples.dtype)

        m, c = kmeans_ndarray(samples, n_clusters, max_iterations)
        fig, ax = plt.subplots(1, 1)
        ax.imshow(m)
        fig.savefig('temp/kmeans.png')

        return torch.from_numpy(m).unsqueeze(0), image2tensor('temp/kmeans.png'), c
