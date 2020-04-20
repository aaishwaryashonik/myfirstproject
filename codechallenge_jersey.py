frst_name=input('Enter your first name: ')
lst_name=input('Enter your last name: ')
if(len(frst_name)<10 and len(lst_name)<10):
    print(frst_name+' '+lst_name)
elif(len(frst_name)>=10 and len(lst_name)<10):
    print(frst_name[0]+'. '+lst_name)
elif(len(frst_name)<10 and len(lst_name)>=10):
    print(frst_name+' '+lst_name[0]+'.')
else:
    print(lst_name)
