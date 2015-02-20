#! /usr/bin/env python

import matplotlib.pyplot as pl
import numpy as np

x = np.arange(-8 * np.pi, 8 * np.pi, 0.01)
y = np.sin(x)
zeros = np.zeros(x.size)

pl.plot(x, y, "b-")
pl.fill_between(x, zeros, y, facecolor='blue', alpha=0.8)

pl.show()
