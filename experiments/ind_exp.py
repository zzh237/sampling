from experiments.ui_args import create_args
import os
from datetime import datetime
from experiments.exp_interface import * 
import matplotlib.pyplot as plt
from web.app import * 
import shutil
from experiments.nuts_exp import * 
from experiments.hmc_exp import * 

colordict = {'hmc':'green','nuts':'blue'}

def run_exp(exp_interface)->dict:
    params = create_args() #as long as the compiler see the parse arg, it starts to receive args from the terminal
    args = params['args']
    distribution = params['distribution']
    start_time = datetime.now()
    filename = exp_interface.filename
    exp_name = filename.split('_')[0]
    args.out_dir = os.path.join('result', filename, start_time.strftime("%Y%m%d-%H%M%S"))
    exp_interface.prepare_exp(args, distribution)
    samples = exp_interface.generate_sample()
    time_duration = datetime.now() - start_time
    result = {'distribution':distribution,
        'sample':samples,
        'time': time_duration,
        'args':args,
        'exp_name': exp_name
        }
    if args.save_result:     
        output_path = os.path.join(args.out_dir, 'sample_result.npy')
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        np.save(output_path, result)
    if args.draw_result:
        path = draw(result['distribution'], result['sample'], result['args'].out_dir, result['time'], result['exp_name'])
        shutil.copyfile(path, os.path.join('web/static/{}.jpg'.format(exp_name)))
        run_app().run(host='127.0.0.1',port=5000, debug=False)
    return result


def draw(dis, samples, dir, exp_time, exp_name)->str:
    fig, ax = plt.subplots(1, 1, sharey=True, figsize = (10,7))
    temp = np.random.multivariate_normal(dis['mean'], dis['cov'], size=int(samples.shape[0]/10))
    ax.scatter(temp[:, 0], temp[:, 1], marker='.', label='Target',color='red')
    ax.scatter(samples[:, 0], samples[:, 1],0.1, marker='o', label=exp_name,color=colordict[exp_name]) 
    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.05,
                     box.width, box.height * 0.95])
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15),fancybox=True, shadow=True, ncol=3)
    title = "Sampling Method VS. Given Target"
    ax.set_title(title, fontsize=15, fontweight='bold')
    fig.text(0.7, 0.2, "sampling time:{:.3f}".format(exp_time.total_seconds()), va='center', rotation='horizontal')
    path = os.path.join(dir, '{}.png'.format(exp_name))
    plt.savefig(path)
    return path



if __name__ == "__main__":
    run_exp(hmc_exp())
        

    


# class ind_exp():
#     """[run individual sampling algorithm]
#     """
#     def __init__(self, exp_interface):
#         params = create_args()
#         self.args = params['args']
#         self.distribution = params['distribution']
#         self.exp = exp_interface

#     def prepare_exp(self):
#         """[initialize the program directory and args, parameters]
#         """
#         now = datetime.now()
#         filename = self.exp.filename
#         self.args.out_dir = os.path.join('result', filename, now.strftime("%Y%m%d-%H%M%S"))
#         self.exp.prepare_exp(self.args, self.distribution)

#     def generate_sample(self):
#         """[summary]

#         Returns:
#             [np.ndarray]: [generate samples from each algorithm]
#         """
#         samples = self.exp.generate_sample()
#         return samples 
    
    # samples = samples[1::10, :]
    # print('Mean: {}'.format(np.mean(samples, axis=0)))
    # print('Stddev: {}'.format(np.std(samples, axis=0)))