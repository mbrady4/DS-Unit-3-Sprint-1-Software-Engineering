#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmePRoductTests(unittest.TestCase):
    '''Making sure Acme products are the best!'''
    def test_default_produce_price(self):
        '''Test default produce price being 10.'''
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_weight(self):
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_stealability_explode(self):
        prod = Product(name='Test', price=100, weight=25, flammability=0.2)

        # Test Stealability Method
        steal = prod.stealability()
        self.assertEqual(steal, 'Very stealable!')

        # Test Explode Method
        flames = prod.explode()
        self.assertEqual(flames, '...fizzle.')


class AcmeReportTests(unittest.TestCase):

    def test_default_num_products(self):
        prods = generate_products()
        self.assertEqual(len(prods), 30)

    def test_legal_names(self):
        prods = generate_products()
        for prod in prods:
            start, end = prod.name.split(' ')
            self.assertIn(start, ADJECTIVES)
            self.assertIn(end, NOUNS)

if __name__ == '__main__':
    unittest.main()
