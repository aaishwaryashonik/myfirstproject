from datetime import date
from datetime import timedelta 

today=date.today()
print('Today is: '+str(today))

yesterday=date.today()-timedelta(days=1)
print('Yesterday was: '+ str(yesterday))


print('Enter any date: ')
datee=date(int(input('Year: ')),int(input('Month: ')),int(input('Date: ')))+  timedelta(days=7)
print('Date one week from the date entered : '+str(datee))

