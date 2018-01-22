from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass


#Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        self.price=price
    def display(self):
        print("Title: {}\n".format(title) +
                   "Author: {}\n".format(author) +
                   "Price: {}\n".format(price))
        return

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()