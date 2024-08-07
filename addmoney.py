import pandas as pd
def add_money():
    data=pd.read_csv('bankdata.csv')
    acno=int(input("Enter account number"))
    acdata=list(data['account'])
    if(acno in acdata):
        amount=int(input("Enter the amount"))
        ind=acdata.index(acno)
        data['balance'][ind]=data['balance'][ind]+amount
        data.to_csv('bankdata.csv',index=False)
        print("Money added successfully")
        print("Current balance ",data['balance'][ind])
    else:
        print("invalid account")
