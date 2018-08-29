# 24/08/2018 - https://www.codingdojo.org/kata/Potter/

from lec9.potter_kata import *

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


# test basic
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


# No discount
def test_basket_countTotalPrice_buyTwoSameBooks_noDiscount_ut():
    first_book = Book('Potter1', 8.0)
    second_book = Book('Potter1', 8.0)

    basket = Basket()
    basket.add_book(first_book)
    basket.add_book(second_book)

    assert basket.count_total_price() == 16.0


# simple discount
def test_basket_countTotalPrice_buyTwoDiffBooks_fivePercentOfDiscount_ut():
    first_book = Book('Potter1', 8.0)
    second_book = Book('Potter2', 8.0)

    basket = Basket()
    basket.add_book(first_book)
    basket.add_book(second_book)

    assert basket.count_total_price() == 15.2     # 15.2 = (0.95 * 16.0)


def test_basket_countTotalPrice_buyThreeDiffBooks_tenPercentOfDiscount_ut():
    first_book = Book('Potter1', 8.0)
    second_book = Book('Potter4', 8.0)
    third_book = Book('Potter2', 8.0)

    basket = Basket()
    basket.add_book(first_book)
    basket.add_book(second_book)
    basket.add_book(third_book)

    assert basket.count_total_price() == 21.6     # 21.6 = (0.90 * 24.0)


def test_basket_countTotalPrice_buyFourDiffBooks_twentyPercentOfDiscount_ut():
    first_book = Book('Potter1', 8.0)
    second_book = Book('Potter2', 8.0)
    third_book = Book('Potter3', 8.0)
    fourth_book = Book('Potter5', 8.0)

    basket = Basket()
    basket.add_book(first_book)
    basket.add_book(second_book)
    basket.add_book(third_book)
    basket.add_book(fourth_book)

    assert basket.count_total_price() == 25.6     # 25.6 = (0.80 * 32.0)


def test_basket_countTotalPrice_buyFiveDiffBooks_twentyFivePercentOfDiscount_ut():
    first_book = Book('Potter1', 8.0)
    second_book = Book('Potter2', 8.0)
    third_book = Book('Potter3', 8.0)
    fourth_book = Book('Potter4', 8.0)
    fifth_book = Book('Potter5', 8.0)

    basket = Basket()
    basket.add_book(first_book)
    basket.add_book(second_book)
    basket.add_book(third_book)
    basket.add_book(fourth_book)
    basket.add_book(fifth_book)

    assert basket.count_total_price() == 30.0     # 30.0 = (0.75 * 40)


# several discounts
def test_basket_countTotalPrice_buyTwoSameOneDiffBooks_mixedDiscountNonePlusFive_ut():
    first_book = Book('Potter1', 8.0)
    second_book = Book('Potter1', 8.0)
    third_book = Book('Potter2', 8.0)

    basket = Basket()
    basket.add_book(first_book)
    basket.add_book(second_book)
    basket.add_book(third_book)

    assert basket.count_total_price() == 8 + 15.2


def test_basket_countTotalPrice_buyPairOfTwoDiffBooks_fivePercentDiscount_ut():
    first_book = Book('Potter1', 8.0)
    second_book = Book('Potter1', 8.0)
    third_book = Book('Potter2', 8.0)
    fourth_book = Book('Potter2', 8.0)

    basket = Basket()
    basket.add_book(first_book)
    basket.add_book(second_book)
    basket.add_book(third_book)
    basket.add_book(fourth_book)

    assert basket.count_total_price() == 30.4     # 30.4 = (0.95 * 32.0)


def test_basket_countTotalPrice_buySixDiffBooks_mixedDiscountTwentyPlusFive_ut():
    first_book = Book('Potter1', 8.0)
    second_book = Book('Potter1', 8.0)
    third_book = Book('Potter2', 8.0)
    fourth_book = Book('Potter3', 8.0)
    fifth_book = Book('Potter3', 8.0)
    sixth_book = Book('Potter4', 8.0)

    basket = Basket()
    basket.add_book(first_book)
    basket.add_book(second_book)
    basket.add_book(third_book)
    basket.add_book(fourth_book)
    basket.add_book(fifth_book)
    basket.add_book(sixth_book)

    assert basket.count_total_price() == 25.6 + 15.2     # 30.4 = (0.8 * 32.0 + 0.95 * 16)


def test_basket_countTotalPrice_buySixDiffBooks_mixedDiscountNonePlusTwentyFive_ut():
    first_book = Book('Potter1', 8.0)
    second_book = Book('Potter1', 8.0)
    third_book = Book('Potter2', 8.0)
    fourth_book = Book('Potter3', 8.0)
    fifth_book = Book('Potter4', 8.0)
    sixth_book = Book('Potter5', 8.0)

    basket = Basket()
    basket.add_book(first_book)
    basket.add_book(second_book)
    basket.add_book(third_book)
    basket.add_book(fourth_book)
    basket.add_book(fifth_book)
    basket.add_book(sixth_book)

    assert basket.count_total_price() == 38.0     # 38.0 = (0.75 * 40.0 + 8.0)


def test_basket_countTotalPrice_buyPairsOfThreeFirstBooksAndFourthAndFifthBooks_twentyPercentDiscount_ut():
    first_book = Book('Potter1', 8.0)
    second_book = Book('Potter1', 8.0)
    third_book = Book('Potter2', 8.0)
    fourth_book = Book('Potter2', 8.0)
    fifth_book = Book('Potter3', 8.0)
    sixth_book = Book('Potter3', 8.0)
    seventh_book = Book('Potter4', 8.0)
    eighth_book = Book('Potter5', 8.0)

    basket = Basket()
    basket.add_book(first_book)
    basket.add_book(second_book)
    basket.add_book(third_book)
    basket.add_book(fourth_book)
    basket.add_book(fifth_book)
    basket.add_book(sixth_book)
    basket.add_book(seventh_book)
    basket.add_book(eighth_book)

    assert basket.count_total_price() == 51.2     # 51.2 = (0.8 * 64)
