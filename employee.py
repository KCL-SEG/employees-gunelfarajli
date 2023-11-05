"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def hourly_pay_calculator(self, wage, hours):
        result = wage * hours 
        return result 
    
    def commission_calculator(self, commission, contract_num):
        result = commission * contract_num
        return result

    def get_pay(self, pay, pay_type, hours = 0, commission = 0, contract_num = 0):
        result = 0
        if pay_type == "Salary":
            if commission and contract_num == 0:
                result = pay + commission
                print(f"{self.name} works on a monthly salary of {pay} and receives a bonus commission of {commission}. Their total pay is {result}.")
            elif commission:
                result = pay + self.commission_calculator(commission, contract_num)
                print(f"{self.name} works on a monthly salary of {pay} and receives a commission for {contract_num} contract(s) at {commission}/contract. Their total pay is {result}.")
            else:
                 result = pay
                 print(f"{self.name} works on a monthly salary of {pay}. Their total pay is {result}")
        elif pay_type == "Hourly":
            total_pay = self.hourly_pay_calculator(pay, hours)
            if commission and contract_num == 0:
                result = total_pay + commission
                print(f"{self.name} works on a contract of {hours} hours at {pay}/hour and receives a bonus commission of {commission}. Their total pay is {result}.")
            elif commission:
                result = total_pay + self.commission_calculator(commission, contract_num)
                print(f"{self.name} works on a contract of {hours} hours at {pay}/hour and receives a commission for {contract_num} contract(s) at {commission}/contract. Their total pay is {result}.")
            else:
                result = total_pay
                print(f"{self.name} works on a contract of {hours} hours at {pay}/hour. Their total pay is {result}.")
        return result
    def __str__(self):
        return self.name


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')
billie.get_pay(4000,"Salary", 0, 0, 0)
# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')
charlie.get_pay(25,"Hourly",100,0,0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')
renee.get_pay(3000, "Salary", 0, 200, 4)
# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')
jan.get_pay(25,"Hourly",150, 220,3)
# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')
robbie.get_pay(2000, "Salary", 0, 1500,0)
# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
ariel.get_pay(30,"Hourly", 120, 600,0)