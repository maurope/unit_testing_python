# This is the main code

def calculate_total(products):
    total = 0
    for product in products:
        total += product ['price']
    return total

# These are the testing functions

def test_calculate_total_with_empty_list():
    print('prueba')

    assert calculate_total([]) == 0 # This line is the expected results


def test_calculate_total_with_single_product():
    products = [
        {
            'name': 'Notebook', 'price':5
        }
    ]
    assert calculate_total(products) == 5 # This line is the expected results

def test_calculate_total_with_multiple_products():
    products = [
        {
            'name': 'Notebook', 'price':5
        },
        {
            'name': 'Book', 'price':5
        },
        {
            'name': 'Pen', 'price':2
        }
    ]
    assert calculate_total(products) == 12 # This line is the expected results

# This is how we call the script to run in the terminal

if __name__ == "__main__":
    test_calculate_total_with_empty_list()
    test_calculate_total_with_single_product()
    test_calculate_total_with_multiple_products()
