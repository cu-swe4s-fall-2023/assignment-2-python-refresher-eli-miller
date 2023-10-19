'''
python my_utils.plot_data.py --data "data/{wildcards.country}.txt" --output "plots/{wildcards.country}.png"
'''

import argparse
import sys
import matplotlib.pyplot as plt
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('--data',
                    type=str,
                    help='Data file name',
                    required=True
                    )

parser.add_argument('--output',
                    type=str,
                    help='Output file name',
                    required=True
                    )

parser.add_argument('--label',
                    type=str,
                    help='Y Label for plot',
                    required=False
                    )


args = parser.parse_args()

data = args.data
output = args.output
label = args.label

print(f'Plotting {data} to {output}')

# Data looks like [1, 2, ...]
with open(data, 'r') as f:
    # handle left and right brackets and the newline
    y = f.read().strip('[]\n').split(',')
    y = [float(i) for i in y]


plt.plot(y)
plt.title(data.split('/')[-1].split('_')[0])
plt.xlabel('index')
plt.ylabel(label)
plt.savefig(output)

