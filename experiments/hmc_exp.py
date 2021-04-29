from hmc.hmc import hmcs
import numpy as np 
import pylab as plt
from experiments.exp_interface import * 
import os 
from distribution import * 



class hmc_exp(exp_interface):
    def __init__(self):
        self.filename = os.path.basename(__file__) 

    def prepare_exp(self, args, distribution):

        self.args = args 
        self.distribution = distribution 
         
    def generate_sample(self):
        dist = correlated_normal(self.distribution['cov'])
        samples, lnprob = \
        hmcs(dist.log_likehood_and_grad, self.args.M, self.args.L, \
            self.distribution['theta0'], self.args.epsilon, progress=True)
        return samples 


