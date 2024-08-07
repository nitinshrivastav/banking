import pandas as pd
def modify_account():
    data=pd.read_csv('bankdata.csv')
    acno=int(input('Enter account number'))
    acdata=list(data['account'])
    if(acno in acdata):
        ind=acdata.index(acno)
        print("press 1 for name change")
        print("press 2 for mobile change")
        choice=input("Enter your choice")
        if(choice=='1'):
            name=input("Enter new name")
            data['name'][ind]=name
            data.to_csv('bankdata.csv',index=False)
            print("Name has been modified")
        elif(choice=='2'):
            mobile=int(input("Enter new mobile number"))
            modata=list(data['mobile'])
            if(mobile in modata):
                print("Mobile number already associated with another account")
            else:
                data['mobile'][ind]=mobile
                data.to_csv('bankdata.csv',index=False)
                print("Mobile number has been modified")
        else:
            print("invalid choice")
    else:
        print("Account number not found")
        