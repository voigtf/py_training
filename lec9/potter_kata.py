from typing import List


class Book:

    def __init__(self, title: str, price: float):
        self.__title = title
        self.__price = price

    @property
    def title(self) -> str:
        return self.__title

    @property
    def price(self) -> float:
        return self.__price


class Basket:

    def __init__(self):
        self.__books = []   # type: List[Book]

    def __len__(self) -> int:
        return len(self.__books)

    def add_book(self, book: Book):
        self.__books.append(book)

    def count_total_price(self) -> float:
        if len(self.__books) < 2:
            return sum([book.price for book in self.__books])

        first_book = self.__books[0]
        checked_books = [first_book.title]
        total_price = first_book.price
        discount_value = 0.0
        multiset = []

        for i in range(1, len(self.__books)):
            next_book = self.__books[i]

            if discount_value == 0.0 and (next_book.title not in checked_books):
                checked_books.append(next_book.title)
                discount_value = 0.05

            elif discount_value == 0.05 and (next_book.title not in checked_books):
                checked_books.append(next_book.title)
                discount_value = 0.1

            elif discount_value == 0.1 and (next_book.title not in checked_books):
                checked_books.append(next_book.title)
                discount_value = 0.2

            elif discount_value == 0.2 and (next_book.title not in checked_books):
                checked_books.append(next_book.title)
                discount_value = 0.25

            total_price += next_book.price

        return total_price * (1 - discount_value)

