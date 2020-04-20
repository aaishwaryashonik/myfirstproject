list_num=[]
list_str=[]
N=int(input('Enter the number of items to be entered in the list: '))

print("Enter the order: ")
for i in range(N):
    list_num.append(int(input()))

print("Enter the strings: ")
for i in range(N):
    list_str.append(input())


def print_order(N,list_num,list_str):
    for i in range(N):
        if list_num[i]==min(list_num):
            if list_num[i]==i+1:
                print(list_str[i].capitalize())
            elif len(list_str[i])==list_num[i]:
                print(list_str[i].upper())
            else:
                print(list_str[i].lower())
            return i
            
for i in range(N):
    i=print_order(N,list_num,list_str)
    list_num[i]=N+1

