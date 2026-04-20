class Book:
    def __init__(self, title, author, is_available=True):
        self.title = title
        self.author = author
        self.is_available = is_available

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"{self.title} olindi")
        else:
            print("Kitob mavjud emas")

    def return_book(self):
        self.is_available = True
        print(f"{self.title} qaytarildi")


book1 = Book("O‘tkan kunlar", "Abdulla Qodiriy")
book1.borrow()
book1.return_book()
