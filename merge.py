import pandas as pd

d1 = pd.read_csv('data1.csv',index_col=0)
d2 = pd.read_csv('data2.csv',index_col=0)

d3 = pd.concat([d1,d2]).reset_index()
d3 = d3.drop(columns=['index'])
d3.to_csv('data.csv')