class User :
    def __init__(self,firstName,lastName,email,password,status='inactive'):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.status = status

def create_user():
    firstName = input("Enter your first name: ")
    lastName = input("Enter your last name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    return User(firstName,lastName,email,password)

user1=create_user();
print(f"User created: {user1.firstName} {user1.lastName}, Email: {user1.email}, Status: {user1.status}")
 