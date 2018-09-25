# 24/08/2018 - https://www.codingdojo.org/kata/Potter/

from lec9.potter_kata import *

# data
# price = None  # type: float
# title = None  # type: str

# behavior


def test_book_canCreateBook_noSideEffect_ut():
    book = Book('Potter1', 8.0)

    assert 'Potter1' == book.title
    assert 8.0 == book.price


def test_canCreateBasket_ut():
    basket = Basket()

    assert isinstance(basket, Basket)


# test basic
def test_basket_addBook_addOneBook_OneBookInBasket_ut():
    book = Book('Potter1', 8.0)
    basket = Basket()
    basket.add_book(book)

    assert 1 == len(basket)


def test_basket_addBook_addTwoBooks_TwoBooksInBasket_ut():
    first_book = Book('Potter1', 8.0)
    second_book = Book('Potter2', 8.0)

    basket = Basket()
    basket.add_book(first_book)
    basket.add_book(second_book)

    assert 2 == len(basket)


# No discount
def test_basket_countTotalPrice_buyTwoSameBooks_noDiscount_ut():
    first_book = Book('Potter1', 8.0)

    basket = Basket()
    basket.add_book(first_book)
    basket.add_book(first_book)

    assert 16.0 == basket.count_total_price()


# simple discount
def test_basket_countTotalPrice_buyTwoDiffBooks_fivePercentOfDiscount_ut():
    first_book = Book('Potter1', 8.0)
    second_book = Book('Potter2', 8.0)

    basket = Basket()
    basket.add_book(first_book)
    basket.add_book(second_book)

    assert 15.2 == basket.count_total_price()     # 15.2 = (0.95 * 16.0)


def test_basket_countTotalPrice_buyThreeDiffBooks_tenPercentOfDiscount_ut():
    first_book = Book('Potter1', 8.0)
    second_book = Book('Potter2', 8.0)
    third_book = Book('Potter3', 8.0)

    basket = Basket()
    basket.add_book(first_book)
    basket.add_book(second_book)
    basket.add_book(third_book)

    assert 21.6 == basket.count_total_price()     # 21.6 = (0.90 * 24.0)


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

    assert 25.6 == basket.count_total_price()       # 25.6 = (0.80 * 32.0)


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

    assert 30 == basket.count_total_price()     # 30.0 = (0.75 * 40)


# several discounts
def test_basket_countTotalPrice_buyTwoSameOneDiffBooks_mixedDiscountNonePlusFive_ut():
    first_book = Book('Potter1', 8.0)
    second_book = Book('Potter2', 8.0)

    basket = Basket()
    basket.add_book(first_book)
    basket.add_book(first_book)
    basket.add_book(second_book)

    assert 8 + 15.2 == basket.count_total_price()


def test_basket_countTotalPrice_buyPairOfTwoDiffBooks_fivePercentDiscount_ut():
    first_book = Book('Potter1', 8.0)
    second_book = Book('Potter2', 8.0)

    basket = Basket()
    basket.add_book(first_book)
    basket.add_book(first_book)
    basket.add_book(second_book)
    basket.add_book(second_book)

    assert 30.4 == basket.count_total_price()     # 30.4 = (0.95 * 32.0)


def test_basket_countTotalPrice_buySixDiffBooks_mixedDiscountTwentyPlusFive_ut():
    first_book = Book('Potter1', 8.0)
    second_book = Book('Potter2', 8.0)
    third_book = Book('Potter3', 8.0)
    fourth_book = Book('Potter4', 8.0)

    basket = Basket()
    basket.add_book(first_book)
    basket.add_book(second_book)
    basket.add_book(third_book)
    basket.add_book(fourth_book)
    basket.add_book(first_book)
    basket.add_book(third_book)

    assert 25.6 + 15.2 == basket.count_total_price()     # 30.4 = (0.8 * 32.0 + 0.95 * 16)


def test_basket_countTotalPrice_buySixDiffBooks_mixedDiscountNonePlusTwentyFive_ut():
    first_book = Book('Potter1', 8.0)
    second_book = Book('Potter2', 8.0)
    third_book = Book('Potter3', 8.0)
    fourth_book = Book('Potter4', 8.0)
    fifth_book = Book('Potter5', 8.0)

    basket = Basket()
    basket.add_book(first_book)
    basket.add_book(first_book)
    basket.add_book(second_book)
    basket.add_book(third_book)
    basket.add_book(fourth_book)
    basket.add_book(fifth_book)

    assert 38.0 == basket.count_total_price()     # 38.0 = (0.75 * 40.0 + 8.0)


def test_basket_countTotalPrice_buyPairsOfThreeFirstBooksAndFourthAndFifthBooks_twentyPercentDiscount_ut():
    special_case = True
    first_book = Book('Potter1', 8.0)
    second_book = Book('Potter2', 8.0)
    third_book = Book('Potter3', 8.0)
    fourth_book = Book('Potter4', 8.0)
    fifth_book = Book('Potter5', 8.0)

    basket = Basket(special_case)
    basket.add_book(first_book)
    basket.add_book(second_book)
    basket.add_book(third_book)
    basket.add_book(fourth_book)
    basket.add_book(first_book)
    basket.add_book(second_book)
    basket.add_book(third_book)
    basket.add_book(fifth_book)


    assert 51.2 == basket.count_total_price()     # 51.2 = (0.8 * 64)


def test_basket_countTotalPrice_buy23MixedBooks_mixedDiscountTwentyFivePlusTwenty_ut():
    first_book = Book('Potter1', 8.0)
    second_book = Book('Potter2', 8.0)
    third_book = Book('Potter3', 8.0)
    fourth_book = Book('Potter4', 8.0)
    fifth_book = Book('Potter5', 8.0)

    basket = Basket(True)
    for counter in range(5):
        basket.add_book(first_book)
        basket.add_book(third_book)
        basket.add_book(fourth_book)
    for counter in range (4):
        basket.add_book(second_book)
        basket.add_book(fifth_book)

    assert 141.2 == basket.count_total_price()


def test_basket_countTotalPriceWithCustomDiscount_buyFiveDifferentBooks_twentyPercentDiscount_ut():
    first_book = Book('Potter1', 8.0)
    second_book = Book('Potter2', 8.0)
    third_book = Book('Potter3', 8.0)
    fourth_book = Book('Potter4', 8.0)
    fifth_book = Book('Potter5', 8.0)

    discount_values = {1: 1.00,
                       2: 0.98,
                       3: 0.95,
                       4: 0.90,
                       5: 0.80}

    basket = Basket()
    basket.set_discount_values(discount_values)
    basket.add_book(first_book)
    basket.add_book(second_book)
    basket.add_book(third_book)
    basket.add_book(fourth_book)
    basket.add_book(fifth_book)


    assert 32 == basket.count_total_price()     # 32 = (0.8 * 40)
