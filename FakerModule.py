'''command to install faker module :
 pip install faker
'''

#Faker Module is used to generate FAKE DATA FOR TESTING PURPOSE

from faker import Faker

obj = Faker()
print("Employee Name:=",obj.name())
print("Employee First Name:=",obj.first_name())
print("Employee Last Name:=",obj.last_name())
print("Date:=",obj.date())
print("Email ID:=",obj.email())
print("Random Number:=",obj.random_number())
print("Random Number:=",obj.random_number(5))
print("Random Integer:=",obj.random_int(min=0,max=99999))
print("Role:=",obj.random_element(elements=("Software Engg.","DBA","Tester","Sales"))) 
