import numpy as np
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: 1 / (1 + e^(-z))
        # return np.round(your_answer, 5)
        e = 2.71828

        res = []

        for i in range(len(z)):
            val = 1 / (1 + e ** (-z[i]))
            res.append(val)
        return np.round(np.array(res), 5)
        pass

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: max(0, z) element-wise
        res = []

        for i in range(len(z)):
            val = max(0.0, z[i])
            res.append(val)

        return np.round(np.array(res), 5)
        pass
