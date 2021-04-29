import numpy as np
from numpy import log, exp, sqrt
from nonuturn.helpers import progress_range
from nonuturn.nuts import leapfrog

def hmcs(f, M, L, theta0, epsilon,progress=False):
    """[summary]

    Args:
        f ([type]): [description]
        M ([type]): [description]
        theta0 ([type]): [description]
        epsilon ([type]): [description]
        L ([type]): [description]
        progress (bool, optional): [description]. Defaults to False.

    Raises:
        ValueError: [description]

    Returns:
        [type]: [description]
    """
    if len(np.shape(theta0)) > 1:
        raise ValueError('theta0 is expected to be a 1-D array')

    D = len(theta0)
    
    samples = np.empty((M, D), dtype=float)
    lnprob = np.empty(M, dtype=float)

    logp, grad = f(theta0)
    samples[0, :] = theta0
    lnprob[0] = logp

    # Choose a reasonable first epsilon by a simple heuristic.
    epsilon = epsilon

    for m in progress_range(1, M, progress=progress):
        # Resample momenta.
        r0 = np.random.normal(0, 1, D)


        # initialize the parameter values
        samples[m, :] = samples[m - 1, :] # the m-1 still keep not changed
        lnprob[m] = lnprob[m - 1]

        thetatilde = samples[m - 1, :]


        rtilde = r0
        
        
        joint0 = logp - 0.5 * np.dot(r0, r0.T)
        gradtilde = grad[:]
        for i in range(1, L):
            thetatilde, rtilde, gradtilde, logptilde = leapfrog(thetatilde, rtilde, gradtilde, epsilon, f)
        
        #joint lnp of theta and momentum r
        joint = logptilde - 0.5 * np.dot(rtilde, rtilde.T)

        alpha = min(1., np.exp(joint)/np.exp(joint0))
        
        if np.random.uniform() < alpha:
            samples[m, :] = thetatilde[:]
            lnprob[m] = logptilde
            logp = logptilde
            grad = gradtilde[:]

    return samples, lnprob

        
