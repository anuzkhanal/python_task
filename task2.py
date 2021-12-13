def account_balance(transcations):
    
    balance = 0

    for x in transcations:

        if (x.split()[0] == 'D'):
            balance = balance + int(x.split()[1])

        else:
            balance = balance - int(x.split()[1])

    return balance


if __name__== "__main__":

    
    transactions = [
        "D 300",
        "D 300",
        "W 200",
        "D 100",
    ]

    print("Total Balance left in your account is : ", account_balance(transactions))
