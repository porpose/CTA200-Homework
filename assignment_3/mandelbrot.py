import numpy as np

def compute(side, condition):
    """ Return a 2D array filled with calculated Mandelbrot set.
    
        side: side length of the 2D array for plotting

        condition: 0 to show diverging points, 1 to add number of
        iterations required to diverge
    """

    x, y = np.linspace(-side, side, 1000), np.linspace(-side, side, 1000)
    bg = np.full((1000, 1000), 100) # background array for plotting

    for i in range(1000):
        for j in range(1000):
            z = 0
            c = complex(x[j], y[i])
            z = z*z + c             # first iteration
            for k in range(100):
                if np.absolute(z) > 4 and condition == 0:
                    bg[i][j] = 1
                    break
                if np.absolute(z) > 4 and condition == 1:
                    bg[i][j] = k
                    break
                z = z*z + c         # iterate until either k > 100 or 
                                    # conditions are reached
    return bg