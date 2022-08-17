import os
import time

import requests as requests
from tqdm import tqdm

url = 'https://stackoverflow.com/questions?tab=newest&page='
path = './data/'

isExist = os.path.exists(path)
if not isExist:
    os.makedirs(path)

for i in range(25000):
    response = requests.get(url + str(i+1), stream=True)

    filename = path + '~so_' + str(i+1) + '.html'

    with open(filename, "wb") as handle:
        for data in tqdm(response.iter_content()):
            handle.write(data)

    print(filename)
    time.sleep(1)
