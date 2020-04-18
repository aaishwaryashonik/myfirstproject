def calculator():
   first_number =input('Enter the first number:  ')
   second_number=input('Enter the second number:  ')
   operation=input('Enter the operation to be performed:  ')
   
   if operation == "add":
         result=int(first_number)+int(second_number)
         print('Sum of '+ first_number+' and '+second_number+' is : '+str(result))
         exit() 
   elif operation == "subtract":
         result=int(first_number)-int(second_number)
         print('Subtraction of '+ first_number+' and '+second_number +' is : '+str(result))
         exit()
   else:
        print('Error')
        exit()


calculator()        
        
