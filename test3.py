# 1
'''username = 'ERIC MOORE '
atmpin = int(1212)
balance =  int(1000)

atmpinenter = int(input('what is you ATM pin ?'))

if atmpinenter == atmpin :
    print('*'* 25)
    print(f'WELCOME {username}')
    print('*'* 25)

    while  True :
        print("--- Assassin Bank Menu ---")
        print('1. Check Balance')
        print('2. Deposit')
        print('3. withdraw')
        print('4. Exit')

        choice = int(input('choose option:'))

        if choice == 1 :
            print(f'your acc balnce is {balance} ')
        elif choice == 2 : 
            depo = int(input('how nush do you what to deposit ?'))
            balance += depo
            print('deposit succesful ')
        elif choice == 3 :
            withd = int(input('how much do you what to withdraw ?'))
            if withd >balance :
                print('insufisent funds')
            else :
                balance -= withd  
                print(' withdraw succesful')
           
        elif choice == 4 :
            print(f'THANKS FOR YOU TIME {username}')
            break
        else :
            print('WRONG OPTION ')
else  :
    print('Access Denied!')

print('GOOD BYE ')
'''

# 2




