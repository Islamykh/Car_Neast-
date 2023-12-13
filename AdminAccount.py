# Admin Panel 

from main import Model,Prices,Types,Elictric,Hybrid,Gazolien,colors
from main import CarNest

class Admin(CarNest):
    def __init__(self,name,Pas):
        self.name=name
        self.__passw=Pas
        CarNest.__init__(self) 
        
    def ShowItems(self):
        print(f'{self.company} Have Many Types : ',*Types,)
        print('\nThe Elictric Cars Available:\n ') 
        print(Elictric[0:5],'\nModels :',*Model[0:],'\n')
        print(Elictric[5:],'\nModels :',*Model[7:],'\n')
        print(f'Colors Available: {colors}')   
        print('\nThe Hybrid Cars Available:\n ') 
        print(Hybrid,'\n \nModels :',*Model[0:],'\n')
        print(f'Colors Available: {colors}') 
        print('\nThe Gazolien Cars Available:\n ') 
        print(Gazolien,'\n \nModels :',*Model[0:],'\n')
        print(f'Colors Available: {colors}')         
            
    def UpdatItem(self,choice,add,sel):  # The options of admin   
        self.choice=choice
        self.add=add 
        self.select=sel
        if self.choice in ['1','2','3','4','5']:
            if self.choice == '1':  # for Add Car
                if self.select =='1':
                    Elictric.append(self.add)
                    print(f'Elictric Cars After Update: {Elictric}\n')
                    return Elictric
                elif self.select =='2':
                    Hybrid.append(self.add)
                    print(f'Hybrid Cars After Update: {Hybrid}\n')
                    return Hybrid
                elif self.select =='3':
                    Gazolien.append(self.add)
                    print(f'Gazolien Cars After Update: {Gazolien}\n')
                    return Gazolien
                else:
                    pass
            if self.choice =='2': # for add model
                Model.append(self.add)
                print(Model)   
                return Model
            
            elif self.choice =='3': # for editing price
                Prices.append(self.add)
                print(Prices)
                return Prices
            
            elif self.choice =='4':
                colors.append(self.add) 
                print(colors)
                return colors
            else:
                pass 
            
    

        
def Admin1(name,admin1):

    print(f'\nHello {name.title()}')
    print('1- Updating Items\n2- Show Items\n3- Close ')
    Section=input('Where you Like Go? ')
    
    if Section in ['1','2','3']:
        if Section =='1':
            print('\nPlease Enter\n1- Adding Car\n2- Adding Model\n3- Editing Price\n4- Adding Color of Cars\n5- Close ')
            options=input('What you need? ')
            
            if options in ['1','2','3','4','5']:
                if options=='1':
                    print("Please Enter The Type of car that you need add car to\n 1- Elictric  2- Hybrid  3- Gazolien  ")
                    select=input('')
                    item=input('Enter the Item you need to add  ').title()
                    admin1.UpdatItem(options,item,select)
                    Admin1(name,admin1)
    
                    
                elif options=='2' or options =='3' or options=='4':
                    item=input('Enter your updat  ').title()
                    admin1.UpdatItem(options,item,'0')
                    Admin1(name,admin1)
                else:
                    pass
            else:
                print('Sorry! You Must Enter 1,2,3,4,5 Only')
                Admin1(name,admin1)
                
                    
        elif Section =='2':
            admin1.ShowItems()
            Admin1(name,admin1)  
        else:
            pass

    else:
        print('Sorry! You Must Enter 1,2,3 Only')

        Admin1(name,admin1)

    
