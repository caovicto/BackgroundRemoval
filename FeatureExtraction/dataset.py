"""
utils.py

Loading images and datasets
"""

import numpy as np
import scipy as sp
from PIL import Image
from scipy import misc
import cv2
import glob
import tensorflow as tf
from progressbar import ProgressBar

# pbar = ProgressBar()


def loadDataset(folder):
    """

    :param folder:
    :type folder:
    :return:
    :rtype:
    """


def imread(filename):
    """
    Reads files
    :param filename:
    :type filename:
    :return:
    :rtype:
    """
    im = sp.misc.imread(filename)
    return im / 255.0


def imsave(np_image, filename):
    """Save image to file.
    Args:
    np_image: .
    filename: .
    """
    im = sp.misc.toimage(np_image, cmin=-1.0, cmax=1.0)
    im.save(filename)


def imwrite(filename, np_image):
    """Save image to file.
    Args:
    filename: .
    np_image: .
    """
    # im = sp.misc.toimage(np_image, cmin=0, cmax=1.0)
    im = sp.misc.toimage(np_image, cmin=-1.0, cmax=1.0)
    im.save(filename)


def imwrite_batch(filenames, np_images):
    """Save batch images to file.
    Args:
    filenames:
    """
    # TODO
    pass


def imresize(np_image, new_dims):
    """Image resize similar to Matlab.
    This function resize images to the new dimension, and properly handles
    alaising when downsampling.
    Args:
    np_image: numpy array of dimension [height, width, 3]
    new_dims: A python list containing the [height, width], number of rows, columns.
    Returns:
    im: numpy array resized to dimensions specified in new_dims.
    """
    # im = np.uint8(np_image*255)
    im = np.uint8((np_image + 1.0) * 127.5)
    im = Image.fromarray(im)
    new_height, new_width = new_dims
    im = im.resize((new_width, new_height), Image.ANTIALIAS)
    return np.array(im)


def loadImages(path, size=(320, 192)):
    X_data = []
    files = glob.glob(path)

    print("extracting {} files from ".format(len(files))+path)

    for myFile in files:
        image = cv2.imread(myFile)
        X_data.append(tf.cast(imresize(image, size), tf.float32))

    return np.array(X_data)

def transform(img):
    #################
    # TODO: homography transform img to create 4 other images
    ##############
    pass

def addOcclusion(img, occclusion):
    #################
    # TODO: homography transform img to create 4 other images
    ##############
    pass