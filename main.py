from addmoney import add_money
from deleteaccount import delete_account
from forgetaccount import forget_account
from modifyaccount import modify_account
from withdrawmoney import withdraw_money
from createaccount import create_account
while True:
    print("press 1 for account creation")
    print("press 2 for add money")
    print("press 3 for withdrawl money")
    print("press 4 for delete account")
    print("press 5 forget account")
    print("press 6 for modification")
    print("press anythhing to exist")
    choice=int(input("enter choice"))
    if(choice==1):
        create_account()
    elif(choice==2):
        add_money()
    elif(choice==3):
        withdraw_money()
    elif(choice==4):
        delete_account()
    elif(choice==5):
        forget_account()
    elif(choice==6):
        modify_account()
    else:
        print("Invalid choice")
        break