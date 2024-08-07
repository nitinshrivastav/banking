import pandas as pd
def forget_account():
    data=pd.read_csv('bankdata.csv')
    mobile=int(input("Enter mobile number"))
    modata=list(data['mobile'])
    if(mobile in modata):
        ind=modata.index(mobile)
        print("Your account details")
        print(data['account'][ind])
    else:
        print("Mobile number not associated with any account")