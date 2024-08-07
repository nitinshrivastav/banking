import pandas as pd
from accountgenerate import account_generate
def create_account():
    data=pd.read_csv('bankdata.csv')
    name=input("Enter your name")
    mobile=int(input("Enter your mobile number"))
    mo=list(data['mobile'])
    if(mobile in mo):
        print("Account already exist with this mobile number")
    else:
        naveen=account_generate()
        test={'name':[name],'account':[naveen],'mobile':[mobile],'balance':[1000]}
        tt=pd.DataFrame(test)
        data=pd.concat([data,tt],axis=0,ignore_index=True)
        data.to_csv('bankdata.csv',index=False)
        print("Account has been created below are the details")
        print("your name",name)
        print("Your account number",naveen)
        print("Your mobile number",mobile)
        print("Opening balance",1000)