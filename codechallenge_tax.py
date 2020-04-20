price=float(input('How much did you pay: '))
if price == 2.00:
    tax=0.07
    print('Tax rate is: '+str(tax))
elif price == 1.00:
    tax=0.07
    print('Tax rate is: '+str(tax))
    exit()
elif price == 0.50:
    tax=0
    print('Tax rate is: '+str(tax))
    exit()
else:
    print('error')
    
