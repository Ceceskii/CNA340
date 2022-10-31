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