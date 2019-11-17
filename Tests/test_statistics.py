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

    def test_mode(self):
         self.assertEqual(self.statistics.mod(), 1)

    def test_popstand(self):
        self.assertEqual(round(self.statistics.popstand(), 4), 0.2233)

    def test_vpop(self):
         self.assertEqual(self.statistics.vpop(), 0.0498442)

    def test_confidence(self):
         self.assertEqual(self.statistics.confidence(), 0.2232581)

    def test_popuvar(self):
         self.assertEqual(self.statistics.confidence(), 0.2232581)

    def test_sample_mean(self):
         self.assertEqual(self.statistics.sample_mean(), 4)

    def test_zscore(self):
         self.assertEqual(self.statistics.confidence(), 0.2232581)

    def test_samplestand(self):
        self.assertEqual(self.statistics.confidence(), 0.2232581)


if __name__ == '__main__':
    unittest.main()