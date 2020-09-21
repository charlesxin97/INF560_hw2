import json

with open('output1.json') as f:
    x = json.load(f)
y = [3 * i + 6 for i in x['result']]
rs = {'result': y}

with open('output2.json', 'w+') as output_file:
    json.dump(rs, output_file)
output_file.close()