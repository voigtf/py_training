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

        total_price = 0.0
        first_book = self.__books[0]
        sub_basket = [[first_book]]
        remaining_books = []

        # group books - calculating discount purpose
        for i in range(1, len(self.__books)):

            next_book = self.__books[i]
            title_in_sub_basket = False

            for items in sub_basket:
                if next_book.title not in [book.title for book in items]:
                    if len(items) < 4:
                        title_in_sub_basket = False
                        items.append(next_book)
                        break
                    #else:
                    #    remaining_books.append(next_book)
                elif next_book.title in [book.title for book in items]:
                    title_in_sub_basket = True

            if title_in_sub_basket is True:
                sub_basket.append([next_book])

        for items in sub_basket:
            print('Books:')
            print([book.title for book in items])

        # discount and total prize calculation
        for items in sub_basket:
            print('Books:')
            print([book.title for book in items])
            discount_values = {1 : 1.00,
                               2 : 0.95,
                               3 : 0.90,
                               4 : 0.80,
                               5 : 0.75}
            total_price += sum([book.price for book in items]) * discount_values[len(items)]

        return total_price
