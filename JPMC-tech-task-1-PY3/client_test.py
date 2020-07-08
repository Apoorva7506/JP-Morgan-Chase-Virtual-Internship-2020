import unittest
from client3 import *

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [

      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual((getDataPoint(quote)),(quote['stock'],quote['top_bid']['price'],quote['top_ask']['price'],(quote['top_bid']['price']+quote['top_ask']['price'])/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):

    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual((getDataPoint(quote)),(quote['stock'],quote['top_bid']['price'],quote['top_ask']['price'],(quote['top_bid']['price']+quote['top_ask']['price'])/2))
     


  """ ------------ Add more unit tests ------------ """
  def test_price_ABC_is_Zero(self):

    quotes = [
      {'top_ask': {'price': 0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    price_a=(quotes[0]['top_ask']['price']+quotes[0]['top_bid']['price'])/2
    price_b=(quotes[1]['top_ask']['price']+quotes[1]['top_bid']['price'])/2
  
    self.assertEqual(float(getRatio(price_a,price_b)),0.0)


  def test_price_DEF_is_Zero(self):

    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 0, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    price_a=(quotes[0]['top_ask']['price']+quotes[0]['top_bid']['price'])/2
    price_b=(quotes[1]['top_ask']['price']+quotes[1]['top_bid']['price'])/2
  
    self.assertEqual((getRatio(price_a,price_b)),"Error")

  def test_getRatio_greaterThan1(self):

    price_a = 201.78
    price_b = 120.9
    self.assertGreater(float(getRatio(price_a, price_b)), 1)

  def test_getRatio_LessThan1(self):
    price_a = 45.36
    price_b = 69.6
    self.assertLess(float(getRatio(price_a, price_b)), 1)

  def test_getRatio_exactlyOne(self):
    price_a = 200.1
    price_b = 200.1
    self.assertEqual(float(getRatio(price_a, price_b)), 1.0)



if __name__ == '__main__':
    unittest.main()
