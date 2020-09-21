import matplotlib.pyplot as plt

import json

with open('output2.json') as f:
    y = json.load(f)

import json

with open('output1.json') as f:
    x = json.load(f)

plt.scatter(x['result'], y['result'])
plt.savefig('./output3.png')
plt.show()
