# CNE330 Homework: How many months it takes to save the target saving $

This code will help you calculate how many month it takes to save the target saving amount. 
The function should return a -1 if the balance goes below 0 because the spending is too high. 
The function should also return -1 if the target is not reached after 100 months.

## Getting Started

These instructions will install Python on your local machine for demo.

https://www.python.org/downloads/

### Prerequisites

Project requires Python to run.

#### Running

Once installed you can run the program.

python cne330.py


def howManyMonths(start, rate, spending, target):
    month = 0
    start_balance = start
    next_month_balance = 0
    
    while(start_balance < target):                   
        if start_balance < 0:                             
            return -1
        month += 1
        next_month_balance = start_balance * (1 + rate) - spending
        start_balance = next_month_balance  
    return month

Add any additional ways to run the program below:

python cna_demo.py test.txt

##### Thanks

Provide thank yous and attributions here. If someone helped you, you looked at another repository, or another article, provide it here.
