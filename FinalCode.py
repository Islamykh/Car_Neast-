
# Run File:
    
from AdminAccount import Admin1, Admin
from UserAccount import User1,User


def Introduction():
    print('\n',' '*15,'Car Nest For Car Rental\n')
    print('Please Enter 1 if you are User and 2 if you are Admin ')
    IntroSelect=int(input(''))

    if IntroSelect ==1:
        name=input('Please Enter your name: ') 
        passw=input('password: ')    
        user=input('User Name: ')   
        pho=int(input('Phone number: '))  
        user1=User(name, passw, user, pho)
        User1(name, user1)

        return name,user1
    
    elif IntroSelect ==2:
        name=input('Please Enter your name: ') 
        passw=input('password: ')
        admin1=Admin(name, passw)
        Admin1(name,admin1)
        
    else:
        print('Please Try again! You Must Enter 1 or 2 only :) ')
        Introduction()
    
Introduction()



