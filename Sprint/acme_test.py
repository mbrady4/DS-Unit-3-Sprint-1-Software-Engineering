#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, _get_unique_names, _get_mean, \
                        ADJECTIVES, NOUNS


class AcmePRoductTests(unittest.TestCase):
    '''Making sure Acme products are the best!'''
    def test_default_produce_price(self):
        '''Test default product price being 10.'''
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_weight(self):
        '''Test default product weight being 20.'''
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
        '''Test that default number of products is 30'''
        prods = generate_products()
        self.assertEqual(len(prods), 30)

    def test_legal_names(self):
        '''Test that generated product names are valid'''
        prods = generate_products()
        for prod in prods:
            start, end = prod.name.split(' ')
            self.assertIn(start, ADJECTIVES)
            self.assertIn(end, NOUNS)

    def test__get_mean(self):
        '''Test that mean is being calculated correctly'''
        nums = [5, 10, 4, 6, 0]
        result = _get_mean(nums)
        self.assertEqual(result, 5)

    def test__get_unique_names(self):
        '''Test that unique names method works correctly'''
        names = ['Test', 'Test', 'Test', 'Exam']
        result = _get_unique_names(names)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
