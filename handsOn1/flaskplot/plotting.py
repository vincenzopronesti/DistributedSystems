import tempfile
import base64

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from numpy import log, sin, cos, tan

def plot_function (function, xmin, xmax):
    def f(x):
        return eval(function)

    with tempfile.TemporaryFile() as tempf:
        t = np.arange(xmin, xmax, (xmax-xmin)/100)

        fig = matplotlib.figure.Figure()
        axis = fig.add_subplot(1, 1, 1)
        axis.plot(t, f(t))

        fig.savefig(tempf)
        
        tempf.seek(0)
        img = tempf.read()
        return base64.b64encode(img).decode("utf-8")
