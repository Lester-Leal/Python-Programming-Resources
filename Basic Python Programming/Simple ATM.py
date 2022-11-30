# Simple Automated Teller Machine
# Author: Jorn Blaedel Garbosa

bal = 6000 # Initialize balance amount to 6000
php = "P{:,.2f}"
pin = '1234' # Declare constant PIN variable
ctr = 3 # Initialize PIN incorrect limit to 3
count = ctr >= 0
invalid = True

# Loop while limit is not 0
while count:
    pin_input = input('ENTER PIN: ')
    if pin_input == pin:
        count=False
        print('WELCOME!')
        invalid = True 
        while invalid:
            print('\n========================================')
            print('[1] BALANCE INQUIRY')
            print('[2] WITHDRAW')
            print('[3] DEPOSIT')
            print('[4] EXIT')
            print('========================================')
            ch = int(input('ENTER CHOICE: '))

            # 1 performs balance inquiry
            if ch == 1:
                print('ACCOUNT BALANCE IS: ',php.format(bal))

            # 2 performs withdraw transaction
            elif ch == 2:
                invalid_amt = True
                while invalid_amt:
                    wdrawamt = int(input('INPUT \'0\' IF YOU WANT TO CANCEL\nENTER WITHDRAW AMOUNT: '))

                    # Warn user to maintain 100 peso balance in account
                    if wdrawamt > bal-100:
                        print('CAN NOT WITHDRAW',php.format(wdrawamt))
                        print('PLEASE MAINTAIN MINIMUM BALANCE OF 100')
                        print('')
                        invalid_amt = True
                        
                    # If balance is sufficient to withdraw amount, perform withdraw transaction
                    elif wdrawamt <= bal-100 and wdrawamt > 0:
                        bal = bal-wdrawamt
                        print('WITHDRAW SUCCESS! NEW BALANCE: ',php.format(bal))
                        invalid_amt = False

                    # Cancel transaction if input is 0
                    elif wdrawamt == 0:
                        print('TRANSACTION CANCELED!')
                        invalid_amt = False

            # 3 performs deposit transaction
            elif ch == 3:
                depoamt = int(input('TYPE \'0\' TO CANCEL\nENTER DEPOSIT AMOUNT: '))
                invalid_depo = True
                while invalid_depo:

                    # Cancel transaction if input is 0
                    if depoamt == 0:
                        print('TRANSACTION CANCELED!')
                        invalid_depo = False

                    # Else, add deposit amount to current balance
                    else:
                        bal = bal+depoamt
                        print('DEPOSIT SUCCESS! NEW BALANCE: ',php.format(bal))
                        invalid_depo = False
            # 4 terminates the program
            elif ch == 4:
                break
            
            # Maintain invalid to true if input not in choices
            else:
                invalid = True
    # If PIN incorrect
    else:
        ctr = ctr-1 # Decrement PIN attempts limit
        # Print attempts left to log in
        if ctr > 0:
            print('')
            print('INCORRECT PIN!',ctr,'ATTEMPTS LEFT!')
        # Terminate program if PIN incorrect is 3
        else:
            print('')
            print('YOU HAVE USED ALL ATTEMPTS!')
            break