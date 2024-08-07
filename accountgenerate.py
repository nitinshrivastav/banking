import pandas as pd
import random
def account_generate():
    data=pd.read_csv('bankdata.csv')
    acno=list(data['account'])
    ac=random.randrange(1000,10000)
    while(ac in acno):
        ac=random.randrange(1000,10000)
    return ac