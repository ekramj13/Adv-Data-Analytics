#create dictionary for data
Employees = [{'ID': '001', 'Name':'Mary', 'Pay_Rate': 15, 'Hours':40}, 
             {'ID': '002', 'Name':'John', 'Pay_Rate': 22, 'Hours':25}, 
             {'ID': '003', 'Name':'Bob', 'Pay_Rate': 35, 'Hours':4}, 
             {'ID': '004', 'Name':'Mel', 'Pay_Rate': 43, 'Hours':62}, 
             {'ID': '005', 'Name':'Jen', 'Pay_Rate': 17, 'Hours':33},
             {'ID': '006', 'Name':'Sue', 'Pay_Rate': 29, 'Hours':45},
             {'ID': '007', 'Name':'Ken', 'Pay_Rate': 40, 'Hours':36},
             {'ID': '008', 'Name':'Dave', 'Pay_Rate': 20, 'Hours':17}, 
             {'ID': '009', 'Name':'Beth', 'Pay_Rate': 37, 'Hours':37},
             {'ID': '010', 'Name':'Ray', 'Pay_Rate': 16.50, 'Hours':80}
            ]


#see list of names defined in the dictionary
Names = [li['Name'] for li in Employees]
print(Names)


Pay_Rates = [li['Pay_Rate']for li in Employees]
print(Pay_Rates)


#see how many pay rates there are 
len(Pay_Rates)


#calculate salary
for Employee in Employees:

    if Employee['Hours'] <=40:
        salary= Employee['Pay_Rate']*(Employee ['Hours'])
        
    else:
        salary=(Employee['Pay_Rate']*1.5*(Employee['Hours']-40))+(Employee['Pay_Rate']*40)
        
        
    print(Employee['Name']+ ": $",(salary))
    
    
## Extra: Calculating Salary Using User Input

Payrate = input("How much does the employee get paid per hour?")
Hours = input("How many hours did the employee work?")

Payrate = float(Payrate)
Hours = float (Hours)
def salary(Payrate,Hours):
    if Hours <=40:
        salary=Payrate*Hours
        
    elif Hours>40:
            salary=(Payrate*(1.5*(Hours-40))+(Payrate*40))
            
    return salary
            
print("The total amount to be paid is: $",salary (Payrate, Hours))