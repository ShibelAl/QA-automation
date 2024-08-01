import unittest
from models import Product, setup_database


class TestProductOperations(unittest.TestCase):

    def setUp(self):
        self.Session = setup_database()
        self.session = self.Session()

    def tearDown(self):
        self.session.close()

    def test_adding_product(self):
        product = Product(name="first product", price=10.0)
        self.session.add(product)
        self.session.commit()
        self.assertIsNotNone(product.id)

    def test_reading_products(self):
        product = Product(name="second product", price=10.0)
        self.session.add(product)
        self.session.commit()
        fetched_product = self.session.query(Product).filter_by(name="second product").first()
        self.assertIsNotNone(fetched_product)
        self.assertEqual(fetched_product.name, "second product")
        self.assertEqual(fetched_product.price, 10.0)

    def test_updating_product(self):
        product = Product(name="third product", price=10.0)
        self.session.add(product)
        self.session.commit()
        product.price = 12.0
        self.session.commit()
        updated_product = self.session.query(Product).filter_by(name="third product").first()
        self.assertEqual(updated_product.price, 12.0)

    def test_deleting_product(self):
        product = Product(name="fourth product", price=10.0)
        self.session.add(product)
        self.session.commit()
        self.session.delete(product)
        self.session.commit()
        deleted_product = self.session.query(Product).filter_by(name="fourth product").first()
        self.assertIsNone(deleted_product)


if __name__ == '__main__':
    unittest.main()
