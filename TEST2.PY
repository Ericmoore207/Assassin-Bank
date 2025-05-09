# username = 'eric'
# pin = 123
# attept = 0 
# maximum_attept = 3

# while attept < maximum_attept :
#     try:
#      username_input = input('Enter your username- ').lower()
#      pin_input = int(input('Enter you pin- '))
#      break

#     except ValueError :
#        print('wrong' )




def log_in():
    print('login')
    print('welcome to Assassin Bank')
    


def sign_in():
    print('sign in')


def welcome():
    print('*'* 25)
    print('welcome to Assassin Bank')
    print('*'* 25)
    print('1. Sign in')
    print('2. Log in ')
    print('3. Exit')
    print('*'* 25)

    def option():
        while True :
            choice = input('Enter an option: ')

            if choice.isdigit():
                if choice == '1':
                    log_in()
                    break 
                elif choice =='2':
                    sign_in()
                    break
                elif choice == '3':
                        print('Thanks for checking out Assassin Bank ')
                        break
                        
                else:
                    print('Wrong option')
            else:
                print('enter a valid option Try Again:')
                continue

    return option()
    






welcome()


    
     
