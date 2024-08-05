def withdraw_money():
    import pandas as pd
    details=pd.read_csv(r"C:\Users\navee\Desktop\banking\bankdata.csv")
    account_no=int(input("enter your account no: "))
    re_enter_account_no=int(input("confirm your account no: "))
    if (account_no==re_enter_account_no and re_enter_account_no in list(details['account'])):
        for i in details.index:
            if(details['account'][i]==re_enter_account_no):
                Current_balance=(details['balance'][i])
                print("Your current balance is:",Current_balance)
        Amount=int(input("enter amount to withdrawl: "))
        if(Amount<=Current_balance):
            for i in details.index:
                if(details['account'][i]==re_enter_account_no):
                   print("Your update balance is:", details['balance'][i]-Amount)
        else:
            print("you have less bank balance")
    else:
        print("account number not matched")
    
    details=details.to_csv(r"C:\Users\navee\Desktop\banking\bankdata.csv")