from shopping_cart import ShoppingCart
from item_database import ItemDatabase
from unittest.mock import Mock
import pytest



###################################################
##  CREATE FIXTURES TO SET UP CONTEXT FOR TESTS  ##
###################################################

# use these fixtures by passing in as arguments to the tests
# These are created new each time a test is run; i.e. fixtures are not reused across tests


@pytest.fixture
def cart():
    # Include all setup for the cart here...
    return ShoppingCart(5)
    


#################################
##  INDIVIDUAL TEST FUNCTIONS  ##
#################################

def test_can_add_item_to_cart(cart):
    cart.add('apple')
    
    # assert is a python keyword; will check whether or not statement is True
    # if statement is true, line will succeed (evaluate to PASS)
    # if statement is false, line will throw an exception (evaluate to FAIL)
    assert cart.size() == 1


def test_when_item_added_then_cart_contains_item(cart):
    cart.add('apple')

    assert 'apple' in cart.get_items()


def test_when_add_more_than_max_items_should_fail(cart):
    for _ in range(5):
        cart.add('apple')
    
    # we expect the function inside 'with' to throw an error
    # if error is thrown, evaluate to PASS
    # if error is not thrown, evaluate to FAIL
    with pytest.raises(OverflowError):
        cart.add('apple')


def test_can_get_total_price(cart):
    cart.add('apple')
    cart.add('orange')
    
    # initialize an instance of the item database class, from a separate file in this directory
    item_database = ItemDatabase()

    # account for various values to be tested with Mock object
    def mock_get_item(item: str):
        if item == 'apple':
            return 1.0
        if item == 'orange':
            return 2.0

    # MOCK the .get() method of the item_database class, using Mock object from Python's unittest.mock built-in module
    # effectively mocks the behavior of our item_database without it actually being implemented yet
    item_database.get = Mock(side_effect=mock_get_item)

    assert cart.get_total_price(item_database) == 3.0
