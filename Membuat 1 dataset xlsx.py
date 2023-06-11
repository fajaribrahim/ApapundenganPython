import random
import pandas as pd

#membuat dataset acak
dataset = []
for _ in range(5000):
    random_number = round(random.uniform(0,1000), 4)
    dataset.append(random_number)
    
#membuat DataFrame dari dataset
df = pd.DataFrame(dataset, columns= ['Dataset'])

#menyimpan DataFrame ke file excel
df.to_excel('D:/Github/ApapundenganPython/datasetcoba1.xlsx', index= False)
print('Dataset telah disimpan ke dalam format Excel')