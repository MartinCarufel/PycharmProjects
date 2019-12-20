import pandas as pd
from time import sleep

myData = [{'input':'faa', 'index':0, 'value':0, 'start_time':0, 'end_time':10},
          {'input':'faa', 'index':1, 'value':1, 'start_time':10, 'end_time':15},
        {'input':'faa', 'index':2, 'value':0, 'start_time':15, 'end_time':30},
        {'input':'faa', 'index':3, 'value':1, 'start_time':30, 'end_time':35},
        {'input':'faa', 'index':4, 'value':0, 'start_time':35, 'end_time':50}]

df = pd.DataFrame(myData)
print(df)

print('allo','Bonjour','Salut',sep=' *** ',end='')
sleep(2)
print(end='\r')
print('allo',sep=' *** ', end="\r")

