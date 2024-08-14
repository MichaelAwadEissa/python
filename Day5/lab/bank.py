# Bank Account System: Bunce
# Design classes for Bank, Account, and Customer.
# Establish relationships where a Bank has multiple Customers, 
# and a Customer can have multiple Accounts.
# Develop methods for transf
# erring money between accounts, 
# checking balances, and generating account statements.	
class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = {}
    
    def add_customer(self, customer):
        self.customers[customer.name] = customer
        return f"Customer {customer.name} added to {self.name}."
    
    def find_customer(self, customer_name):
        return self.customers.get(customer_name, None)
    
    def transfer_money(self, from_account, to_account, amount):
        from_account_result = from_account.withdraw(amount)
        if "Insufficient funds" not in from_account_result:
            to_account.deposit(amount)
            return f"Transferred ${amount} from Account {from_account.account_number} to Account {to_account.account_number}."
        return from_account_result
    
    def generate_customer_statement(self, customer_name):
        customer = self.find_customer(customer_name)
        if customer:
            accounts = customer.get_all_accounts()
            statements = [account.check_balance() for account in accounts]
            return "\n".join(statements)
        return "Customer not found."

        
class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return f"${amount} deposited. New balance: ${self.balance}"
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount
        return f"${amount} withdrawn. New balance: ${self.balance}"
    
    def check_balance(self):
        return f"Account {self.account_number} balance: ${self.balance}"


# class Customer:
    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.accounts = []
    
    def open_account(self, account_number, initial_deposit=0):
        account = Account(account_number, initial_deposit)
        self.accounts.append(account)
        return f"Account {account_number} opened for {self.name}."
    
    def get_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None
    
    def get_all_accounts(self):
        return self.accounts

        