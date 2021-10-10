import numpy as np
from PIL import Image
from ipywidgets import interact, fixed

# This is the code we provide
# or they can add the resize function themselves, to see how one could adapt this
def imshow(X, resize=None):
    """

    Please enter here a good description.

    """
    l = len(X)

    @interact
    def _imshow(i:(0, l-1)=0, resize=fixed(resize)):
        im = Image.fromarray(X[i])

        if resize:
            im = im.resize(resize)

        return im