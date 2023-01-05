from shopping_cart import ShoppingCart
import pytest

def test_can_add_item_to_cart():
    cart = ShoppingCart(5)
    cart.add('apple')
    
    # assert is a python keyword; will check whether or not statement is True
    # if statement is true, line will succeed (evaluate to PASS)
    # if statement is false, line will throw an exception (evaluate to FAIL)
    assert cart.size() == 1

def test_when_item_added_then_cart_contains_item():
    cart = ShoppingCart(5)
    cart.add('apple')

    assert 'apple' in cart.get_items()

def test_when_add_more_than_max_items_should_fail():
    cart = ShoppingCart(5)
    for _ in range(5):
        cart.add('apple')
    
    # we expect the function inside 'with' to throw an error
    # if error is thrown, evaluate to PASS
    # if error is not thrown, evaluate to FAIL
    with pytest.raises(OverflowError):
        cart.add('apple')

def test_can_get_total_price():
    cart = ShoppingCart(5)
    cart.add('apple')
    cart.add('orange')
    
    # need to set up price_map argument to test function that will take this as an input
    price_map = {
        'apple': 1.0,
        'orange': 2.0
    }

    assert cart.get_total_price(price_map) == 3.0