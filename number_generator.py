import numpy as np
import json

x = np.random.rand(1000)
x = x * 100
rs = {'result': x.tolist()}

with open('output1.json', 'w+') as output_file:
    json.dump(rs, output_file)
output_file.close()