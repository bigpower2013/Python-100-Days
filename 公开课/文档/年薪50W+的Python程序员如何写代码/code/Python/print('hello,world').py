import numpy as np 
import pandas as pd 
s = pd.Series(list(np.random.randint(1,100,4)))
df = pd.DataFrame({'name':list(['wanglxing','wangluoxi','jiaoke','miaomiao']),'score':s})
print(df)

s = ['a','b','c']
ss = list(('a','b','c'))
print(s)
print(ss)
ss  = s
print(ss)
