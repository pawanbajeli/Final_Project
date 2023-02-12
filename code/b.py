# import lib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


i=800
while(i<1000):
  path="./fetched_data/file_"+str(i)+".csv"
  df = pd.read_csv(path)
  matrix1=df.corr().round(2)
  a=plt.figure(figsize=(19,16))
  sns.heatmap(matrix1,annot=True)
  plt.savefig('./images/heatmap_'+str(i)+'.png')
  plt.close()
  print(i, flush=True)
  i=i+1;
