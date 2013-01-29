import unittest
from StringIO import StringIO
from homework_1p5.src import averager, maximum,\
    minimum, data_length, summer


class TestHw1(unittest.TestCase):
    """
    For testing modules in the homework_1p5 repo.
    """
    def setUp(self):
        self.outfile = StringIO()
        commastring = "score\n34\n345\n23\n2354"
        self.commafile = StringIO(commastring)

    def test_compute_average(self):
        result = averager.compute_average(self.commafile)
        self.assertEqual(result, 689.0)

    def test_compute_maximum(self):
        result = maximum.compute_maximum(self.commafile)
        self.assertEqual(result, 2354)

    def test_compute_minimum(self):
        result = minimum.compute_minimum(self.commafile)
        self.assertEqual(result, 23)

    def test_compute_length(self):
        result = data_length.compute_length(self.commafile)
        self.assertEqual(result, 5)

    def test_compute_sum(self):
        result = summer.compute_sum(self.commafile)
        self.assertEqual(result, 2756)

    def tearDown(self):
        self.commafile.close()
