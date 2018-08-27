# 24/08/2018 - https://www.codingdojo.org/kata/Potter/

from Py_training.lec9.potter_kata import *

# data
# price = None  # type: float
# title = None  # type: str

# behavior


def test_book_canCreateBook_noSideEffect_ut():
    book = Book('Potter1', 8.0)

    assert book.title == 'Potter1'
    assert book.price == 8.0


def test_canCreateBasket_ut():
    basket = Basket()

    assert isinstance(basket, Basket)


def test_basket_addBook_addOneBook_OneBookInBasket_ut():
    book = Book('Potter1', 8.0)
    basket = Basket()
    basket.add_book(book)

    assert len(basket) == 1


def test_basket_addBook_addTwoBooks_TwoBooksInBasket_ut():
    first_book = Book('Potter1', 8.0)
    second_book = Book('Potter1', 8.0)

    basket = Basket()
    basket.add_book(first_book)
    basket.add_book(second_book)

    assert len(basket) == 2


def test_basket_countTotalPrice_buyTwoSameBooks_noDiscount_ut():
    first_book = Book('Potter1', 8.0)
    second_book = Book('Potter1', 8.0)

    basket = Basket()
    basket.add_book(first_book)
    basket.add_book(second_book)

    assert basket.count_total_price() == 16.0


def test_basket_countTotalPrice_buyTwoDiffBooks_fiveProcentOfDiscount_ut():
    first_book = Book('Potter1', 8.0)
    second_book = Book('Potter2', 8.0)

    basket = Basket()
    basket.add_book(first_book)
    basket.add_book(second_book)

    assert basket.count_total_price() == 15.2     # 15.2 = (0.95 * 16.0)
