class Book:
    
    def __init__(self, title,author,pages ):
        self.title = title
        self.author = author
        self.pages = pages

new_Book = Book("New Book","michael",543)
print(new_Book.title)


class profile:
    def __init__(self,name, email, language,):
        self.name = name
        self.email = email
        self.language = language


michael_awad = profile("michael awad", "michaelawadeissa@gmail.com", "English", )
print(michael_awad.name)
mariam =profile("mariam", "mariamiti@gmail.com", "English" )
print(mariam.name)


class message:
    def __init__(self, sender, receiver, content,date):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.date = date


new_message = message("michael awad", "mariam", "hello mariam", "2022-12-25")
print(new_message.content)

class product:
    def __init__(self, name, price, quantity,review):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.review = review


new_product = product("Laptop", 1000, 10, "excellent")
print(new_product.name)