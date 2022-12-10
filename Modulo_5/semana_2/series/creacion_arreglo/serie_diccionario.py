import pandas as pd

d = {'a': 1, 'b': 2, 'c': 3}
ser = pd.Series(data=d, index=['a', 'b', 'c'])
noser = pd.Series(data=d, index=['x', 'y', 'z'])
