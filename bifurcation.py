# import dependencies
import numpy as np
import matplotlib.pyplot as plt



class BifurcationDiagram:
    def calBifucation(self, **parameters):
        """
        Calculate the bifurcation points of x and r coordinates.

        Parameters:
        - min_r: Minimum value of the r parameter (float)
        - max_r: Maximum value of the r parameter (float)
        - step_r: Step size for the r parameter (float)
        - max_iterations: Maximum number of iterations (integer)
        - skip_iterations: Number of iterations to skip (integer)

        Returns:
        - Numpy arrays containing the x and r coordinates of the bifurcation diagram
        """
        min_r = parameters["min_r"]
        max_r = parameters["max_r"]
        step_r = parameters["step_r"]
        max_iterations = parameters["max_iters"]
        skip_iterations = parameters["skip_iters"]

        max_counter = int((max_iterations - skip_iterations)
                          * (max_r - min_r) / step_r)
        # The x and r results will be stored in these two arrays
        result_x = np.zeros(max_counter)
        result_r = np.zeros(max_counter)

        # Start the main loop
        i = 0
        for r in np.arange(min_r, max_r, step_r):
            x = 0.1
            for it in range(max_iterations):
                x = r * x * (1-x)
                if it > skip_iterations:
                    result_x[i] = x
                    result_r[i] = r
                    i += 1
        result_x = result_x[result_r != 0].copy()
        result_r = result_r[result_r != 0].copy()

        return result_x, result_r
