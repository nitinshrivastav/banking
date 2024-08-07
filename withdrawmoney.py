import pandas as pd
def withdraw_money():
    data=pd.read_csv('bankdata.csv')
    acdata=list(data['account'])
    account=int(input("Enter your account"))
    if(account in acdata):
        ind=acdata.index(account)
        amount=int(input("Enter the amount"))
        if(amount<data['balance'][ind]):
            data['balance'][ind]=data['balance'][ind]-amount
            data.to_csv('bankdata.csv',index=False)
            print("Money withdrawl successfully")
            print('Current balance',data['balance'][ind])
        else:
            print("Insufficient fund")
    else:
        print("Account doesnot exist")