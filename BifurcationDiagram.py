# import dependencies
import numpy as np
import matplotlib.pyplot as plt
import numba


class BifurcationDiagram:
    def calBifucation(self, **parameters):
        ''' calculate the bifucation points of x and r coordinates\n
        parameters are min_r, max_r, step_r, max_iters, skip_iters'''

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


chaosMap = BifurcationDiagram()
result_x, result_r = chaosMap.calBifucation(
    min_r=3.0, max_r=4.0, step_r=0.0001, max_iters=1000, skip_iters=100)

# Plot the bifucation diagram
plt.figure(figsize=(5, 3), dpi=200)
plt.plot(result_r, result_x, ",", color='k')
plt.show()
