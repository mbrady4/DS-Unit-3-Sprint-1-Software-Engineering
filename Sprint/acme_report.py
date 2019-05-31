import random
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(n=30, price_range=[5, 100], weight_range=[5, 100],
                      flammability_range=[0.0, 2.5]):
    products = []
    for _ in range(n):
        # Set parameters
        start = random.sample(ADJECTIVES, k=1)[0]
        end = random.sample(NOUNS, k=1)[0]
        name = start + ' ' + end
        price = random.randint(price_range[0], price_range[1])
        weight = random.randint(weight_range[0], weight_range[1])
        flammability = random.uniform(flammability_range[0],
                                      flammability_range[1])

        # Create instance of Product Class
        prod = Product(name=name, price=price, weight=weight,
                       flammability=flammability)

        # Append product instance to list of products
        products.append(prod)

    return products


def inventory_report(products):
    names = []
    prices = []
    weights = []
    flammabilities = []
    security_scores = []

    for product in products:
        names.append(product.name)
        prices.append(product.price)
        weights.append(product.weight)
        flammabilities.append(product.flammability)
        security_scores.append(product.security_score)

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print(f'Unique product names: {_get_unique_names(names)}')
    print(f'Average price: {_get_mean(prices)}')
    print(f'Average weight: {_get_mean(weights)}')
    print(f'Average flammability: {_get_mean(flammabilities)}')
    print(f'Average security score: {_get_mean(security_scores)}')


def _get_unique_names(list):
    '''Returns number of unique values in list'''
    return len(set(list))


def _get_mean(list):
    '''Returns mean of numeric values in list'''
    total = 0
    for i in list:
        total += i
    return total / len(list)

if __name__ == '__main__':
    inventory_report(generate_products())
