import pandas as pd
import re

# remove resolution (no longer needed but meh)
def strip_res (str):
    return re.sub(r'\[.*?\]','',str)

# change this to data file you want to strip
titles = pd.read_csv('data30k.csv',index_col=0)

titles.title = titles.title.apply(strip_res)

titles.to_csv('titles.csv')
