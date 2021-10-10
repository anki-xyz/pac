import numpy as np
from PIL import Image
from ipywidgets import interact, fixed

# This is the code we provide
# or they can add the resize function themselves, to see how one could adapt this
def imshow(X, resize=None):
    """

    Please enter here a good description.

    """
    
    im = Image.fromarray(X)

    if resize:
        im = im.resize(resize)

    return im