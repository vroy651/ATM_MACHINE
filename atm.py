class ATM:
    # constructor is special method within it all codes execute automatically whenever its instance is created
    def __init__(self):
        # initialize of atributes
        self.pin = ""
        self.balance = 0

        # initialize of methods
        self.menu()
    def menu(self):
       user_input = input("""
       hello sir or madam,how would you like to proceed?
       1. Enter 1 to create a new pin
       2. Enter 2 to deposit 
       3. Enter 3 to withdraw
       4. Enter 4 to check the balance
       5. Enter 5 to exit
       """)
       if user_input == "1":
            self.create_pin()
       elif user_input == "2":
           self.deposit()
       elif user_input == "3":
           self.withdraw()
       elif user_input == "4":
           self.check_balance()
       else:
           print("thank you!")         
    def create_pin(self):
        self.pin = input("Enter your pin number")
        print("your pin number successfully created")
        self.menu()
        
    def check_balance(self):
       temp=input("Please enter your pin number")
       if temp == self.pin:
            print(self.balance)
       else:
           print("Invalid pin")
       self.menu()
       
    def deposit(self):
        temp=input("Please enter your pin number")
        if temp == self.pin:
            amount=int(input("Enter your amount"))
            self.balance+=amount
            print("deposit successful")
        else:
            print("please enter your your valid pin number")
        self.menu()
        
    def withdraw(self):
       temp=input("Please enter your pin number")
       if temp == self.pin:
            amount=int(input("Enter your amount"))
            
            if amount<self.balance:
              self.balance-=amount
              print("withdraw successful")
              print(f"your current balance of your acount:{self.balance}")
            else:
              print("not a valid withdraw amount")
       else:
           print("invalid pin , please enter a valid pin number")
       self.menu()


# intialize the object of ATM
if __name__ == "__main__":
    obj=ATM()