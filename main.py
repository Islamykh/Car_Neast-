
# File for define all variable

Types= ['Elictric','Hybrid','Gazolien']
Model=[2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023]
Prices=[30,40,50,80,100,120,150]
colors=['Black','White','Gray','Red']
price=0
totalPrice=0

Elictric=['Kia Ev-6','Kia Ev9','Golf','Jetta','Nesan Leafe' ,'Kia Niro','Ioniq',
        'Kona','Id6','Id4','Id3'
        'Tesla Model S','Tesla Model Y', 'Tesla Model 3',
        'Mercedes Eqs','Mercedes Eqc','Mercedes Eqe']

Hybrid=['Kia Sonata','Prius','Prius C','Prius Prime','Kia Optima','Kia Niro',
        'Camry','Corolla','Ford Fusion',
        'Ford C-Max','Ford F-150','Ioniq','Kona','Toyota Crown'
        ,'Honda Civic','Honda Accord','Honda Clarity','Honda Insight',
        'Mercedes Glc','Mercedes C 350E','Mercedes Eqs']

Gazolien=['Accent', 'Elantra','Avanti','Hyundai Genesis','Kia Cerato',
            'Peugeot 3008 ','Peugeot 208',
            'PMW 3 Series','PMW 5 Series','PMW 7 Series', 'Mercedes','Audi',
            'Land Rover','Reng Rover'] 

# main Class

class CarNest:
    
    location ='Irbid-Jordan'
    WorkingHour= '8:00 AM - 10:00 PM '
    company='Car Nest '
    Created= '2023'
    Owner= 'Eng. Islam Khashashneh'
    contact=+962776464640
    
            
    def About(self):
        print(f'Company Name: {self.company}\n')
        print(f'Working Hour : {self.WorkingHour}\n')
        print(f'Established in: {self.Created}\n')
        print(f"Designed by: {self.Owner}\n")
        print(f"Phone Number: {self.contact}\n")
        print('Our Location: {self.location}\n')
    
    



