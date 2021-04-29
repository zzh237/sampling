from experiments.ui_args import create_args
import os
from datetime import datetime
from experiments.exp_interface import * 
import matplotlib.pyplot as plt
from web.app import * 
import shutil
from experiments.nuts_exp import * 
from experiments.hmc_exp import * 
from experiments.ind_exp import draw

colordict = {'hmc':'green','nuts':'blue'}

def run_exp(hmc_, nuts_)->dict:
    params = create_args() #as long as the compiler see the parse arg, it starts to receive args from the terminal
    args = params['args']
    distribution = params['distribution']
    start_time = datetime.now()
    exp_name = os.path.basename(__file__).split('.')[0]
    args.out_dir = os.path.join('result', exp_name, start_time.strftime("%Y%m%d-%H%M%S"))
    hmc_.prepare_exp(args, distribution)
    hmc_samples = hmc_.generate_sample()
    hmc_time_duration = datetime.now() - start_time
    start_time = datetime.now()
    nuts_.prepare_exp(args, distribution)
    nuts_samples = nuts_.generate_sample()
    nuts_time_duration = datetime.now() - start_time
    result = {'distribution':distribution,
        'hmc_sample':hmc_samples,
        'hmc_time': hmc_time_duration,
        'nuts_sample':nuts_samples,
        'nuts_time': nuts_time_duration,
        'args':args,
        'exp_name': exp_name
        }
    if args.save_result:     
        output_path = os.path.join(args.out_dir, 'sample_result.npy')
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        np.save(output_path, result)
    if args.draw_result:
        hmc_path = draw(result['distribution'], result['hmc_sample'], result['args'].out_dir, result['hmc_time'], 'hmc')
        shutil.copyfile(hmc_path, os.path.join('web/static/hmc.jpg'))
        hmc_path = draw(result['distribution'], result['nuts_sample'], result['args'].out_dir, result['nuts_time'], 'nuts')
        shutil.copyfile(hmc_path, os.path.join('web/static/nuts.jpg'))
        run_app().run(host='127.0.0.1',port=5000, debug=False)
    return result

if __name__ == "__main__":
    run_exp(hmc_exp(),nuts_exp())





