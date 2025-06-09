import time

print("Please insert the card")
time.sleep(2)

password = 3249
pin = int(input("\nEnter your ATM pin : "))

balance = 20000

while True:
    if (pin == password):
        print('''
1. Balance
2. Withdraw
3. Dipost  
4. Exit  
            ''')
        try:
            optional = int(input("Enter your option : "))
        except:
            print("Enter the valid option. ")

        if (optional == 1):
            print(f"\nYour balance :: {balance}")
            print("--------------------------------")
        

        if (optional == 2):
            amount = int(input("Enter withdraw amount:- "))
            if(amount <= balance):
                balance -= amount
                print(f"\nAmount withdrawed is : {amount} ")
                print(f"\n Updataed balance : {balance}")
                print("--------------------------------")
            else:
                print("Enter the valid amount.")
                print("--------------------------------")

        if (optional == 3):
            amount = int(input("Enter diposted amount: "))
            balance += amount
            print(f"\n Remaninig balance : {balance}")
            print("--------------------------------")

        if (optional == 4):
            print("------------- Trancistion exit -------------")
            break
            

    else:
        print("Entered worng pin")