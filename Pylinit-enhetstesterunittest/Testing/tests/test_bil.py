import unittest
from src.bil import Bil

class TestBil(unittest.TestCase):
  def test_antal_hjul(self):
    min_bil = Bil(bilInfo = ["Volkswagen Golf", 300000, False], True, False)
    self.assertEqual(min_bil.hjul, 4)
    min_bil.bränsletest()
    min_bil.radio_test()
    min_bil.acceleration_förändring()
    min_bil.aktivera_fdw()
