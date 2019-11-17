import unittest

from Statistics.statistics import Statistics


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics('Tests/Data/statistics.csv')

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_decorator_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean(self):
        self.assertEqual(self.statistics.mean(), 0.25)

    def test_median(self):
        self.assertEqual(self.statistics.median(), 4)

    #def test_mode(self):
   #     self.assertEqual(self.statistics.mod(), 1)

    #def test_psd(self):
    #    self.assertEqual(round(self.statistics.psd(), 4), 0.2233)

    #def test_vpp(self):
    #    self.assertEqual(self.statistics.vpp(), 0.0498442)


if __name__ == '__main__':
    unittest.main()