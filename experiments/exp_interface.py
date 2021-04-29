from abc import ABC, abstractclassmethod
import numpy as np 

class exp_interface(ABC):
    def prepare_exp(self):
        raise NotImplementedError
    def generate_sample(self)->np.ndarray:
        """Generate the samples as nd array, with size N, D

        Raises:
            NotImplementedError: [description]

        Returns:
            np.ndarray: [description]
        """
        raise NotImplementedError 