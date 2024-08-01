def add_money():
    import pandas as pd
    details=pd.read_csv(r"C:\Users\navee\Desktop\Banking project\banking\bankdata.csv")
    box=list(details['account'])
    account_no=int(input("enter your account no: "))
    re_enter_account_no=int(input("confirm your account no: "))
    if (account_no==re_enter_account_no and account_no in box):
        index=box.index(account_no)
        new_balance=(details['balance'][index])    
    else:
        print("account no not matched")
    Enter_amount=int(input("enter amount to add: "))
    Final_balance=new_balance+Enter_amount
    print("your amount have been added successfully and updated balance is", Final_balance) 