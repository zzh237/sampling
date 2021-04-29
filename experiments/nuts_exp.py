
from nonuturn.nuts import nuts6
import numpy as np 
import pylab as plt
from experiments.exp_interface import * 
import os 
from distribution import * 



class nuts_exp(exp_interface):
    def __init__(self):
        self.filename = os.path.basename(__file__) 

    def prepare_exp(self, args, distribution):

        self.args = args 
        self.distribution = distribution 
         
    def generate_sample(self):
        dist = correlated_normal(self.distribution['cov'])
        samples, lnprob, epsilon = \
        nuts6(dist.log_likehood_and_grad, self.args.M, self.args.Madapt, \
            self.distribution['theta0'], self.args.delta, progress=True)
        return samples 
    
    
        
        







