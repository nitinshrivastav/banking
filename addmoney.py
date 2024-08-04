def add_money():
    import pandas as pd
    details=pd.read_csv(r"C:\Users\navee\Desktop\banking\bankdata.csv")
    account_no=int(input("enter your account no: "))
    re_enter_account_no=int(input("confirm your account no: "))
    if (account_no==re_enter_account_no and re_enter_account_no in list(details['account'])):
        Amount=int(input("enter amount to be added: "))
    for i in details.index:
        if(details['account'][i]==re_enter_account_no):          #Question can we remove this line
            print("Your Final balance is: ",details['balance'][i]+Amount)            
    else:
        print('account number not matched')
    details=details.to_csv(r"C:\Users\navee\Desktop\banking\bankdata.csv",index=False)
def add_money()