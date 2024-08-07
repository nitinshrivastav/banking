import pandas as pd
def delete_account():
    data=pd.read_csv('bankdata.csv')
    ac1=int(input("Enter account number"))
    ac2=int(input("Re enter account number"))
    if(ac1==ac2):
        if(ac1 in list(data['account'])):
            ind=list(data['account']).index(ac1)
            data=data.drop(ind,axis=0)
            data=data.reset_index(drop=True)
            data.to_csv('bankdata.csv',index=False)
            print("Your account has been deleted")
        else:
            print("Account number not exist")
    else:
        print("Account number not match")