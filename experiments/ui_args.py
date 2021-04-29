
import argparse 
import numpy as np 
def create_args()->dict:
    """[summary]

    Returns:
        dict: [a dictionary contains the args and non args parameters]
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--D', default=2, type=int, 
                        help='dimension of sample')
    parser.add_argument('-m', '--M', default=5000, type=int,
                        help='number of sample size')
    
    ## nuts parameter
    parser.add_argument('-ma', '--Madapt', default=5000, type=int,
                        help='Madapt')
    
    parser.add_argument('-da', '--delta', default=0.2, type=float, 
                        help='delta used')
    
    
    ## hmc parameter
    parser.add_argument('-ep', '--epsilon', default=0.1, type=float, 
                        help='epsilon used')
    
    parser.add_argument('-l', '--L', default=10, type=int, 
                        help='L leapfrog steps envolved')
    


    parser.add_argument('-od', '--out_dir', default='', type=str, 
                        help='output directory')
    parser.add_argument('-s','--save_result', default=True, type=bool, 
                        help='save result to local or not')
   
    parser.add_argument('-draw','--draw_result', default=True, type=bool, 
                        help='draw result or not')
    args = parser.parse_args()


    theta0 = np.random.normal(0, 1, args.D)
    mean = np.zeros(args.D)
    cov = np.asarray([[1, 1.98], 
                    [1.98, 4]])
    params = {'distribution':{'theta0':theta0, 'mean':mean,'cov':cov}, 'args':args}
    return params

    