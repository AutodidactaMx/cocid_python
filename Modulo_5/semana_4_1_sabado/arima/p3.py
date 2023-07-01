"""
En este caso haremos dos diferencias para  revisar  como nos da autocorrelacion 
y luego  volver a realizar la prueba
"""
import pandas as pd
from statsmodels.tsa.stattools import adfuller

df=pd.read_csv('./AirPassengers.csv')
df.set_index('Month',inplace=True)
df.index=pd.to_datetime(df.index)

'''
Solo se necesita si la series estacionaria. De lo contrario, no se necesita diferenciación, es decir, d = 0.
'''
#Primera diferenicacion p = 1.
diff1 = df.diff()

#Segunda diferenicacion p = 2.
diff2 = df.diff().diff()

"""Ahora nuevamente  probaremos la prueba Dickey Fuller para las dos diferenciaciones"""
#Segunda prueba con los datos de diferenciacion 1
result=adfuller(diff1.dropna().values)
result_dict = dict(zip([' Primera diferenicacion (ADF Test)', 'pvalue', 'usedlag', 'nobs', 
                        'critical' 'values', 'icbest'],result))
print(result_dict)

#Tercera prueba con los datos de diferenciacion 2
result=adfuller(diff2.dropna().values)
result_dict = dict(zip(['Segunda diferenicacion (ADF Test)', 'pvalue', 'usedlag', 'nobs', 
                        'critical' 'values', 'icbest'],result))
print(result_dict)

'''
Para la serie anterior, la serie temporal alcanza la estacionariedad con dos ordenes de diferenciación
'''