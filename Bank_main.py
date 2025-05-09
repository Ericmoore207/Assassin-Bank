username = "eric"
atmpin = int(1)
balance = int(1000)
atmpinenter = int(input('what is your atm pin?'))


if atmpinenter == atmpin :
    print(f'welcome {username}')
    chbaq = input('do you what to check you acc balance type ("yes" or "no")?')
    if chbaq == "yes" :
        print(f'your acc balance is  {balance}')
    else:
        print()

    depoq =  input('do you what to deposit to your acc  type ("yes" or "no")?')
    if depoq == "yes" :
        deposit_amount = int(input('how mush do you what to deposit?'))
        balance = balance + deposit_amount

    else:
        print()

    check_balance = input('do you what to check you acc balance type ("yes" or "no")?')
    if check_balance == "yes" :
        print(f'your acc balance is  {balance}')
    else:
        print()

    withq = input('do you what to withdraw from your acc  type ("yes" or "no")?')
    if depoq == "yes":
       withdraw_amount = int(input('how mush do you what to withdraw?'))
       balance = balance - withdraw_amount

    else:
        print()

    check_balance = input('do you what to check you acc balance type ("yes" or "no")?')
    if check_balance == "yes" :
        print(f'your acc balance is  {balance}')
    else:
        print()

    exitq = input('do you what to exit type ("yes" or "no")')
    if exitq == 'yes' :
        print('Thanks for using Assassin Bank')
    else :
        print()

else :
    print('access deniald ')

print('thank you ')













































