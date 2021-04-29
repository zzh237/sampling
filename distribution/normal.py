import numpy as np 

class correlated_normal():
    def __init__(self, cov):
        self.precision = np.linalg.inv(cov)
    def log_likehood_and_grad(self, theta):
        """ Example of a target distribution that could be sampled from using NUTS.  (Doesn't include the normalizing constant.)
        Note: 
        cov = np.asarray([[1, 1.98],
                        [1.98, 4]])
        """

        #A = np.linalg.inv( cov )
        
        # A = np.asarray([[50.251256, -24.874372],
        #                 [-24.874372, 12.562814]])

        if not hasattr(self, 'precision'):
            raise AttributeError("precision matrix doesn't exist")
        grad = -np.dot(theta, self.precision)
        logp = 0.5 * np.dot(grad, theta.T)
        return logp, grad
