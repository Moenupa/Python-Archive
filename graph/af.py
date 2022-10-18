import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def get_df(quantity, average=False):
    TFC = np.array((500, 1000, 2000))
    AVC = np.array((1, 0.8, 0.6))
    
    if average:
        data = {
            'AFC': TFC / quantity,
            'AVC': AVC,
        }
    else:
        data = {
            'TFC': TFC,
            'TVC': AVC * quantity,
        }

    df = pd.DataFrame(
        data=data,
        index=('Machine A', 'Machine B', 'Machine C')
    )
    
    return df

if __name__ == '__main__':
    quantity = (2000, 4000, 6000)
    average = (True, False)
    
    for q in quantity:
        for a in average:
            df = get_df(q, a)
            ax = df.plot.bar(stacked=True, label=True)
            ax.legend(loc='lower right', fancybox=True, framealpha=0.5)
            for bars in ax.containers:
                ax.bar_label(bars)
            plt.savefig(f"./graph/af_q{q}_{'atc' if a else 'tc'}.png", transparent=True, bbox_inches='tight')