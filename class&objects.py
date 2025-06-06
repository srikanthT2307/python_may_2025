# write a python program for the laptop using class and objects
# class laptop_details():
#     def __init__(self,brand,ram,price):
#         self.brand = brand
#         self.ram = ram
#         self.price = price
#     def uasge(self):
#         print(f"the laptop {self.brand} is very good for regular uasge")
#     def pricage(self):
#         print(f" the laptop {self.brand} is come with very resonable price {self.price}")
#     def storage(self):
#         print(f"laptop you buyed {self.brand} has very good innbuilt {self.ram} GB")
# object1 = laptop_details('Lenovo',16,45000)
# object1.uasge()
# object1.pricage()
# object1.storage()

# write a python code for ATM program using class,objects and inhertance:
# single inhertance

# class ATM():
#     def __init__(self,bankname,branch,place):
#         self.bankname = bankname
#         self.branch = branch
#         self.place = place
#     def withdrawal(self):
#         print(f"Please visit again {self.bankname} with {self.branch} at {self.place}")
#     def deposit(self):
#         print(f"Please visit again {self.bankname} with {self.branch} at {self.place}")
#     def enquiry(self):
#         print(f"Please visit again {self.bankname} with {self.branch} at {self.place}")
# service = ATM('ICICI','Ongole-Sujathanagar','Ongole')
# service.withdrawal()
# service.enquiry()


# Multiple inhertance:
# class ATM():
#     def __init__(self,bankname,branch,place):
#         self.bankname = bankname
#         self.branch = branch
#         self.place = place
# class Customer_features(ATM):
#     def withdrawal(self):
#         print(f"Please visit again {self.bankname} with {self.branch} at {self.place}")
#     def deposit(self):
#         print(f"Please visit again {self.bankname} with {self.branch} at {self.place}")
# class enquiry(ATM):
#     def enquiry(self):
#         print(f"Please visit again {self.bankname} with {self.branch} at {self.place}")
# service = enquiry('ICICI','Ongole-Sujathanagar','Ongole')
# # service.withdrawal()
# # service.deposit()
# service.enquiry()