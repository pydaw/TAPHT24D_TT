import logging
from behave import given, when, then

# logging.basicConfig(level=logging.INFO)

cart_books = list()
cart_prices = list()
cart_items = list()

def add_item_to_cart(title, price):
    logging.info(f"add_item_to_cart(title={title}, price={price})")

    if cart_books.count(title) > 0:
        index = cart_books.index(title)
        cart_items[index] += 1
    else: 
        cart_books.append(title)
        cart_prices.append(price)
        cart_items.append(1)
    
    logging.info(f"cart_books: {cart_books}")
    logging.info(f"cart_prices: {cart_prices}")
    logging.info(f"cart_items: {cart_items}")

def remove_item_in_cart(title):
    logging.info(f"remove_item_in_cart(title={title})")
    index = cart_books.index(title)
    cart_books.pop(index)
    cart_prices.pop(index)
    cart_items.pop(index)

def number_of_items_in_cart():
    logging.info("number_of_items_in_cart()")
    items = 0
    for number_of_items in cart_items:
        items += number_of_items
    logging.info(f"items: {items}")
    return items

def occurrence_of_book_title_in_cart(title):
    logging.info(f"occurrence_of_book_title_in_cart({title})")
    occurrence = cart_items[cart_books.index(title)]
    logging.info(f"occurrence: {occurrence}")
    return occurrence

def total_price_in_cart():
    logging.info("total_price_in_cart()")
    total_price = 0
    for i in range(len(cart_books)):
        total_price += (cart_prices[i] * cart_items[i])
    logging.info(f"total price: {total_price}")
    return total_price

def book_titles_in_cart():
    book_titels = str(cart_books).replace("[","").replace("]","").replace("'","")
    logging.info(f"book titles: {book_titels}")
    return book_titels

def empty_cart():
    logging.info("empty_cart()")
    cart_books.clear()
    cart_prices.clear()
    cart_items.clear()
    logging.info(f"cart_books: {cart_books}")
    logging.info(f"cart_prices: {cart_prices}")
    logging.info(f"cart_items: {cart_items}")


@given(u'användaren befinner på sidan med böcker')
def step_given_book_page(context):
    context.page = "books_page"


@when(u'när användaren trycker på knappen "lägg i varukorg" för bok "{book}" med priset "{price}"')
def step_when_press_add_to_cart(context, book, price):
    context.book = book
    context.price = int(price)
    add_item_to_cart(context.book, context.price)
    

@then(u'skall varukorgen innehålla böckerna "{books}" och ange antal "{number_of_books}" samt aktuellt pris "{total_price}"')
def step_impl(context, books, number_of_books, total_price):
    assert book_titles_in_cart() == books
    assert number_of_items_in_cart() == int(number_of_books)
    assert total_price_in_cart() == int(total_price)


@given(u'användaren befinner sig på varukorgsidan')
def step_given_cart_page(context):
    context.page = "cart_page"


@given(u'varukorgen innehåller "{books}"')
def step_given_books_in_cart(context, books):
    empty_cart()
    if "bok1" in books:
        add_item_to_cart("bok1", 100)
    
    if "bok2" in books:
        add_item_to_cart("bok2", 200)
    
    if "bok3" in books:
        add_item_to_cart("bok3", 300)


@when(u'användaren trycker på papperskorgen för "{book}"')
def step_when_remove_books(context, book):
    remove_item_in_cart(book)


@then(u'boken skall tas bort från varukorgen och visa pris "{total_price}" samt antal "{number_of_books}"')
def step_then_no_books_in_cart(context, total_price, number_of_books):
    assert total_price_in_cart() == int(total_price)
    assert number_of_items_in_cart() == int(number_of_books)


@when(u'när användaren trycker på knappen "lägg i varukorg" för boken "Ubuntu som Server" 2 gånger')
def step_when_add_same_book_twice(context):
    context.book_title = "Ubuntu som Server"
    context.book_price = 200

    # Add book once
    add_item_to_cart(context.book_title, context.book_price)
    
    # Add same book twice
    add_item_to_cart(context.book_title, context.book_price)

    # Check cart
    context.same_book_result_occurrence = occurrence_of_book_title_in_cart(context.book_title)


@then(u'antalet av boken "Ubuntu som Server" skall vara 2 i varukorgen')
def step_then_book_twice_in_cart(context):
    assert context.same_book_result_occurrence == 2

@when(u'användaren trycker på "töm varukorg"')
def step_when_empty_cart(context):
    empty_cart()
    

@then(u'varukorgen skall vara tom och summan skall vara noll')
def step_then_cart_empty(context):
    assert number_of_items_in_cart() == 0
    assert total_price_in_cart() == 0