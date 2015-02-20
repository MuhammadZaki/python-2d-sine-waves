#! /usr/bin/env python

import matplotlib.pyplot as pl
import numpy as np

x = np.arange(-4 * np.pi, 4 * np.pi, 0.01)
y1 = np.sin(2 * x)
y2 = np.sin(x + (0.5 * np.pi))

zeros = np.zeros(x.size)

pl.hold(True)

pl.plot(x, y1, "b-")
pl.plot(x, y2, "r-")
pl.plot(x, y1 + y2, "g-")


#pl.fill_between(x, zeros, y1, facecolor='blue', alpha=0.5)
#pl.fill_between(x, zeros, y2, facecolor='red', alpha=0.5)
pl.fill_between(x, zeros, y1 + y2, facecolor='green', alpha=0.5)

pl.show()
