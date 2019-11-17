import unittest
from Calculator.calculator import Calculator
from Statistics.statistics import Statistics
from CsvReader.readpop import read_pop


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics('Tests/Data/statistics.csv')
        self.calculator=Calculator()

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

    def test_prop(self):
        self.assertEqual(self.statistics.prop(), 1.6)

    def test_variance_sample_proportion(self):
        my_pop = read_pop("Variance.csv")
        try:
            self.assertEqual(self.calculator.variance_sample_proportion(my_pop),0.0045) # positive test
            self.assertNotEqual(self.calculator.variance_sample_proportion(my_pop),0.0045+1)   # negative test
        except AssertionError as e:
            print("Variance of Sample Proportion has Assertion Error:", e)


    def test_standardised_score(self):
        self.assertListEqual(self.statistics.zscore(), 0.2232581)

if __name__ == '__main__':
    unittest.main()