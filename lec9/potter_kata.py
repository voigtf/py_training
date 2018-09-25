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

    def __init__(self, special_case=False):
        self.__books = []   # type: List[Book]
        self.discount_values = {1: 1.00,
                                2: 0.95,
                                3: 0.90,
                                4: 0.80,
                                5: 0.75}
        self.special_case = special_case
        if self.special_case:
            self.sub_basket_limit = 4
        else:
            self.sub_basket_limit = 5

    def __len__(self) -> int:
        return len(self.__books)

    def add_book(self, book: Book):
        self.__books.append(book)

    def set_discount_values(self, discount_values: dict):
        self.discount_values = discount_values

    def count_total_price(self) -> float:

        total_price = 0.0
        sub_basket = []
        title_found_in_sub_basket = False

        for book in self.__books:

            if sub_basket == []:
                sub_basket.append([book])

            elif len(sub_basket) > 0:

                for items in sub_basket:

                    if book.title in [books.title for books in items] and len(items):
                        title_found_in_sub_basket = True

                    elif book.title not in [books.title for books in items] and len(items) < self.sub_basket_limit:
                        title_found_in_sub_basket = False
                        items.append(book)
                        break

                    elif len(items) == self.sub_basket_limit:
                        title_found_in_sub_basket = True

                if title_found_in_sub_basket:
                    sub_basket.append([book])

        for items in sub_basket:
            print([book.title for book in items])
            total_price += sum([book.price for book in items]) * self.discount_values[len(items)]

        return total_price
