# User Panel :
    
from main import Model,Prices,Elictric,Hybrid,Gazolien,colors,Types
from main import CarNest


class User(CarNest):
    def __init__(self,n,pa,us,pho):
        self.Name=n
        self.Password= pa
        self.UserName=us
        self.Phone=pho
    
    def ShowCars(self,sel):
        self.sel=sel
        print(f'{self.company} Have Many Types : ',*Types,)
        
        if self.sel in ['1','2','3']:
            if self.sel =='1':
                print('\nThe Elictric Cars Available:\n ') 
                print(Elictric[0:5],'\nModels :',*Model[0:],'\n')
                print(Elictric[5:],'\nModels :',*Model[7:],'\n')
                print(f'Colors Available: {colors}')   

                
            elif self.sel == '2':
                print('\nThe Hybrid Cars Available:\n ') 
                print(Hybrid,'\n \nModels :',*Model[0:],'\n')
                print(f'Colors Available: {colors}') 
        
            elif self.sel =='3':
                print('\nThe Gazolien Cars Available:\n ') 
                print(Gazolien,'\n \nModels :',*Model[0:],'\n')
                print(f'Colors Available: {colors}')   

            else:
                pass
        else:
            print('Sorry! You Must Enter 1,2,3 Only ')  
        
    def ShowPrice(self,ch,m):
        self.Car=ch
        self.model= m
        
        if self.model in Model: 
            if self.Car.title() in Elictric[0:5]: # 'Kia Ev-6','Kia Ev9','Golf','Jetta','Nesan Leafe'
                if self.model in Model[3:7]: # 2017-2019
                    print(f'the price of {self.Car.title()} for one day is {Prices[0]}')
                elif self.model in Model[7:]: #2020-2023
                        print(f'the price of {self.Car.title()} for one day is {Prices[1]}')
                else:  # less than 2013 or ,more than 2023
                    print('Sorry! This Model Not Availabile. ') 
                    
            elif self.Car.title() in Elictric[5:9]:  # Kia Niro','Ioniq','Kona'
                if self.model in Model[7:]: # 2020-2023
                        print(f'the price of {self.Car.title()} for one day is {Prices[3]}')
                else:
                    print('Sorry! This Model Not Availabile. ')   
                    
            elif self.Car.title() in Elictric[9:13]: #'Id6','Id4','Id3''Tesla Model S','Tesla Model Y', 'Tesla Model 3'
                if self.model in Model[7:]: # 2020-2023
                        print(f'the price of {self.Car.title()} for one day is {Prices[4]}')
                else:
                    print('Sorry! This Model Not Availabile. ') 
                    
            elif self.Car.title() in Elictric[13:]: #'Mercedes'
                if self.model in Model[6:]: # 2020-2023
                        print(f'the price of {self.Car.title()} for one day is {Prices[6]}')
                else:
                    print('Sorry! This Model Not Availabile. ')    
            
            elif self.Car.title() in Hybrid [0:4]:# 'Kia Sonata','Prius','Prius C','Prius Prime'
                if self.model in Model[0:7]:
                    print(f'the price of {self.Car.title()} for one day is {Prices[0]}')
                elif self.model in Model[7:]:
                    print(f'the price of {self.Car.title()} for one day is {Prices[1]}')
                    
            elif self.Car.title() in Hybrid [4:14]:# 'Kia Optima','Kia Niro','Camry','Corolla','Ford Fusion', 
            #'Ford C-Max','Ford F-150','Ioniq','Kona','Toyota Crown'
                if self.model in Model[0:7]:
                    print(f'the price of {self.Car.title()} for one day is {Prices[1]}')
                elif self.model in Model[7:]:
                        print(f'the price of {self.Car.title()} for one day is {Prices[2]}')
                
                    
            elif self.Car.title() in Hybrid [14:18]: #'Honda Civic','Honda Accord','Honda Clarity','Honda Insight'
                if self.model in Model[0:7]:
                    print(f'the price of {self.Car.title()} for one day is {Prices[2]}')
                elif self.model in Model[7:]:
                        print(f'the price of {self.Car.title()} for one day is {Prices[3]}')
                else:
                    print('Sorry! This Model Not Availabile. ') 
                    
            elif self.Car.title() in Hybrid [18:]:  #Mercedes
                if self.model in Model[0:5]:
                    print(f'the price of {self.Car.title()} for one day is {Prices[2]}')
                elif self.model in Model[5:8]:
                        print(f'the price of {self.Car.title()} for one day is {Prices[3]}')
                elif self.model in Model[8:]:
                        print(f'the price of {self.Car.title()} for one day is {Prices[-2]}')
                
                    
            elif self.Car.title() in Gazolien[0:7]: #'Accent', 'Elantra','Avanti','Hyundai Genesis',
            #'Kia Cerato','Peugeot 3008 ','Peugeot 208
                if self.model in Model[0:7]:
                    print(f'the price of {self.Car.title()} for one day is {Prices[0]}')
                elif self.model in Model[7:]:
                        print(f'the price of {self.Car.title()} for one day is {Prices[1]}')
                
            elif self.Car.title() in Gazolien[0:12]  :#'PMW 3 Series','PMW 5 Series','PMW 7 Series', 
            #'Mercedes','Audi'
                if self.model in Model[0:5]:
                    print(f'the price of {self.Car.title()} for one day is {Prices[3]}')
                elif self.model in Model[5:8]:
                        print(f'the price of {self.Car.title()} for one day is {Prices[4]}')
                elif self.model in Model[8:]:
                        print(f'the price of {self.Car.title()} for one day is {Prices[-1]}')
                
            elif self.Car.title() in Gazolien[12:]: #'Land Rover','Reng Rover'
                if self.model in Model[0:5]:
                    print(f'the price of {self.Car.title()} for one day is {Prices[3]}')
                elif self.model in Model[5:8]:
                        print(f'the price of {self.Car.title()} for one day is {Prices[5]}')
                elif self.model in Model[8:]:
                        print(f'the price of {self.Car.title()} for one day is {Prices[-1]}')
            
            else:
                print('Sorry! This Car Not Availabile. ') 
                
        else:
            print('Sorry! This Model Not Availabile. Car Neast have {Model} only:)') 
                
    def RentCar (self,c,m,col,da):
            self.Car = c
            self.model=m
            self.color=col
            self.days=da
            
            if self.model in Model:
                if self.color.title() in colors:
                    if self.Car.title() in Elictric[0:5]: # 'Kia Ev-6','Kia Ev9','Golf','Jetta','Nesan Leafe'
                        if self.model in Model[3:7]: # 2017-2019
                            totalPrice=Prices[0]*self.days                
                            print(f'You are Select {self.Car.title()}, for {self.days} days, so the total Price is {totalPrice}')
                            return totalPrice
                        elif self.model in Model[7:]: #2020-2023
                            totalPrice=Prices[1]*self.days                
                            print(f'You are Select {self.Car.title()}, for {self.days} days, so the total Price is {totalPrice}') 
                            return totalPrice 
                    elif self.Car.title() in Elictric[5:9]:  # Kia Niro','Ioniq','Kona'
                        if self.model in Model[7:]: # 2020-2023
                            totalPrice=Prices[3]*self.days                
                            print(f'You are Select {self.Car.title()}, for {self.days} days, so the total Price is {totalPrice}') 
                    
                    elif self.Car.title() in Elictric[9:13]: #'Id6','Id4','Id3''Tesla Model S','Tesla Model Y', 'Tesla Model 3'
                        if self.model in Model[7:]: # 2020-2023
                            totalPrice=Prices[4]*self.days                
                            print(f'You are Select {self.Car.title()}, for {self.days} days, so the total Price is {totalPrice}')
                            return totalPrice
                    elif self.Car.title() in Elictric[13:]: #'Mercedes'
                        if self.model in Model[6:]: # 2020-2023
                            totalPrice=Prices[6]*self.days                
                            print(f'You are Select {self.Car.title()}, for {self.days} days, so the total Price is {totalPrice}')
                            return totalPrice

                    elif self.Car.title() in Hybrid [0:4]:# 'Kia Sonata','Prius','Prius C','Prius Prime'
                        if self.model in Model[0:7]:
                            totalPrice=Prices[0]*self.days                
                            print(f'You are Select {self.Car.title()}, for {self.days} days, so the total Price is {totalPrice}')
            
                        elif self.model in Model[7:]:
                            totalPrice=Prices[1]*self.days                
                            print(f'You are Select {self.Car.title()}, for {self.days} days, so the total Price is {totalPrice}')
                            return totalPrice

                        
                    elif self.Car.title() in Hybrid [4:14]:# 'Kia Optima','Kia Niro','Camry','Corolla','Ford Fusion', 'Ford C-Max','Ford F-150','Ioniq','Kona','Toyota Crown'
                        if self.model in Model[0:7]:
                            totalPrice=Prices[1]*self.days                
                            print(f'You are Select {self.Car.title()}, for {self.days} days, so the total Price is {totalPrice}')
            
                        elif self.model in Model[7:]:
                            totalPrice=Prices[2]*self.days                
                            print(f'You are Select {self.Car.title()}, for {self.days} days, so the total Price is {totalPrice}')
                            return totalPrice

                    elif self.Car.title() in Hybrid [14:18]: #'Honda Civic','Honda Accord','Honda Clarity','Honda Insight'
                        if self.model in Model[0:7]:
                            totalPrice=Prices[2]*self.days                
                            print(f'You are Select {self.Car.title()}, for {self.days} days, so the total Price is {totalPrice}')
                            return totalPrice

                        elif self.model in Model[7:]:
                            totalPrice=Prices[3]*self.days                
                            print(f'You are Select {self.Car.title()}, for {self.days} days, so the total Price is {totalPrice}')
                            return totalPrice

                            
                    elif self.Car.title() in Hybrid [18:]:  #Mercedes
                        if self.model in Model[0:5]:
                            totalPrice=Prices[2]*self.days                
                            print(f'You are Select {self.Car.title()}, for {self.days} days, so the total Price is {totalPrice}')
                            return totalPrice

                        elif self.model in Model[5:8]:
                            totalPrice=Prices[2]*self.days                
                            print(f'You are Select {self.Car.title()}, for {self.days} days, so the total Price is {totalPrice}')
                            return totalPrice

                        elif self.model in Model[8:]:
                            totalPrice=Prices[3]*self.days                
                            print(f'You are Select {self.Car.title()}, for {self.days} days, so the total Price is {totalPrice}')
                            return totalPrice

                            
                    elif self.Car.title() in Gazolien[0:7]: #'Accent', 'Elantra','Avanti','Hyundai Genesis','Kia Cerato','Peugeot 3008 ','Peugeot 208
                        if self.model in Model[0:7]:
                            totalPrice=Prices[0]*self.days                
                            print(f'You are Select {self.Car.title()}, for {self.days} days, so the total Price is {totalPrice}')
                            return totalPrice

                        elif self.model in Model[7:]:
                            totalPrice=Prices[1]*self.days                
                            print(f'You are Select {self.Car.title()}, for {self.days} days, so the total Price is {totalPrice}')
                            return totalPrice

                            
                    elif self.Car.title() in Gazolien[0:12]  :#'PMW 3 Series','PMW 5 Series','PMW 7 Series', 'Mercedes','Audi'
                        if self.model in Model[0:5]:
                            totalPrice=Prices[3]*self.days                
                            print(f'You are Select {self.Car.title()}, for {self.days} days, so the total Price is {totalPrice}')
                            return totalPrice

                        elif self.model in Model[5:8]:
                            totalPrice=Prices[4]*self.days                
                            print(f'You are Select {self.Car.title()}, for {self.days} days, so the total Price is {totalPrice}')
                            return totalPrice

                        elif self.model in Model[8:]:
                            totalPrice=Prices[-1]*self.days                
                            print(f'You are Select {self.Car.title()}, for {self.days} days, so the total Price is {totalPrice}')
                            return totalPrice

                            
                    elif self.Car.title() in Gazolien[12:]: #'Land Rover','Reng Rover'
                        if self.model in Model[0:5]:
                            totalPrice=Prices[3]*self.days                
                            print(f'You are Select {self.Car.title()}, for {self.days} days, so the total Price is {totalPrice}')
                            return totalPrice

                        elif self.model in Model[5:8]:
                            totalPrice=Prices[5]*self.days                
                            print(f'You are Select {self.Car.title()}, for {self.days} days, so the total Price is {totalPrice}')
                            return totalPrice

                        elif self.model in Model[8:]:
                            totalPrice=Prices[6]*self.days                
                            print(f'You are Select {self.Car.title()}, for {self.days} days, so the total Price is {totalPrice}')
                            return totalPrice

                    else:
                        print('Sorry! This Car Not Availabile.') 

                else:
                    print('Sorry! This Color Not Availabile. Car Neast have {colors} only:)') 

            else:
                print('Sorry! This Model Not Availabile. Car Neast have {Model} only:)') 
                    


def checkout(name,Choice,model,days,color,user1):
    print('\nWould you like to confirm your order? \n1-Comfirm order \n2-You need other Car\n3-Close')
    checkout=input('')
    if checkout in ['1','2','3']:
        if checkout == '1':
            location=input('Please Enter Your Location to Drive the car to you ')
            date=input('Please Enter The date that you need the car')
            time=input('what is the best time for you? \n')
            print(f'{Choice.title()} Model {model} {color.title()}, will drive to {location.title()}, at {date}  {time.upper()}','\n')
            print(f'{name.title()}, We appreciate your choice of our website and wish you satisfaction and certainty in your decision. \n')
        elif checkout =='2':
            User1(name,user1)
        else:
            pass
    else:
        print('Sorry You Must Enter 1,2,3 only')
        User1(name,user1)

        
        
def User1 (name,user1):
    print(f'\nWelocm {name.title()} ')
    print('1- About \n2- Show Cars\n3- Show Prices\n4- Rent Cars\n5- Close')
    ChoiceSection=input('Where you Like Go?  ')
    print('\n')
    if ChoiceSection in ['1','2','3','4','5']:
        if ChoiceSection =="1":
            intro=CarNest()
            intro.About()
            User1 (name,user1)
        elif ChoiceSection =='2':
            print(f'{name.title()}, What is the Type you need to show:\n1- For Electric\n2- For Hybrid\n3- For Gazolien')
            selection=(input('? '))
            user1.ShowCars(selection)
            User1 (name,user1)
        elif ChoiceSection =='3':
            Choice=input("What car you need ? ").title()
            model =int(input('What The Model? '))
            user1.ShowPrice(Choice, model)
            User1 (name,user1)
        elif ChoiceSection =='4':
            Choice=input("What your Choice ? ").title()
            model =int(input('What your Model? '))
            days=int(input('How many days you need the car? '))
            color=input('What the Color you need? ')
            user1.RentCar(Choice,model,color,days)
            checkout(name,Choice,model,days,color,user1)
            
        elif ChoiceSection =='5':
            pass
        
    else:
        print('Sorry You Must Enter 1,2,3,4,5 only')
        User1(name,user1)
        



    
