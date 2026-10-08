class ATMConstants:
    withdraw = 1
    deposit = 2
    balance_check = 3

option = 1

match option:
    case ATMConstants.withdraw:
        print("Withdraw")
    case ATMConstants.deposit:
        print("Deposit")
    case ATMConstants.balance_check:
        print("Balance Check")
    case _:
        print("Invalid option")