# python_task
TASK 1

Python function which returns a list of all of the numbers which are divisible by 7, but not divisible by 5, between 2000 and 3200

TASK 2

Python function that returns the balance of a bank account as an integer, based on a list of transactions. The balance of the account is 0 at the beginning.

transactions = [
        "D 300",
        "D 300",
        "W 200",
        "D 100",
    ]
    
Where W = withdraw, and D = deposit
    
the balance of the bank account should be 500

TASK 3

Python function, that first creates a dictionary where the dictionary keys are numbers 1 through x (1, 2, 3, ..., x) and 
the values are the keys squared (1, 4, 9, ..., x**2). 
The function should then use this dictionary in order to finally return a string containing "1**2=1, 2**2=4, 3**2=9, ..., x**2=??.

TASK 4

The Finnish Patent and Registration Office (PRH) offers an open API, where you can access information about public companies in Finland.
A guide for accessing this API can be found here: https://avoindata.prh.fi/index_en.html, and more specifically https://avoindata.prh.fi/tr_en.html. 
Get familiar with the given API, and implement a Python program that is capable of answering these questions:

How many limited companies (companyForm==OY) have been registered to the municipality of Ylitornio (registeredOffice==Ylitornio) after the date 1978-3-14? 
How many of them have ceased to exist?
Similarly as above, what is the amount of registered and the amount of ceased limited companies for the municipality of Merikarvia? 
How about for Parikkala?
The program should utilize the open PRH API and print a report that features answers for these questions.
