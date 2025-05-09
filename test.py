username = 'eric'
atmpin = int(1212)
balance =  int(1000)


while True :
    try :
        username_input = input('what is yhour username?').lower
        atmpinenter = int(input('what is you ATM pin ?'))
        break
        

    except ValueError:

        print('Access Denied!, wrong crendential')

        
        print("\n" + "-"*40)
        print(f'💳 Welcome to Assassin Bank, {username}')
        print('-'* 40)


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



