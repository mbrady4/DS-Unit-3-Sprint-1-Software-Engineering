import random
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(n=30):
    products = []
    for _ in range(n):
        # Set parameters
        start = random.sample(ADJECTIVES, k=1)[0]
        end = random.sample(NOUNS, k=1)[0]
        name = start + ' ' + end
        price = random.randint(5,100)
        weight = random.randint(5,100)
        flammability = random.uniform(0.0, 2.5)

        # Create instance of Product Class
        prod = Product(name=name, price=price, weight=weight, flammability=flammability)

        # Append product instance to list of products
        products.append(prod)

    return products


def inventory_report(products):
    names = []
    prices = []
    weights = []
    flammabilities = []

    for product in products:
        names.append(product.name)
        prices.append(product.price)
        weights.append(product.weight)
        flammabilities.append(product.flammability)

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print(f'Unique product names: {len(set(names))}')
    print(f'Average price: {_get_mean(prices)}')
    print(f'Average weight: {_get_mean(weights)}')
    print(f'Average flammability: {_get_mean(flammabilities)}')


def _get_mean(list):
    total = 0
    for i in list:
        total += i
    return total / len(list)

if __name__ == '__main__':
    inventory_report(generate_products())
