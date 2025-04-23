import unittest
import os
import sys
from unittest.mock import MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from shadow.polyedr import Polyedr


class TestPolyedr(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
        cls.test_file_modify1 = os.path.join(cls.data_dir, 'modify1.geom')
        cls.test_file_modify2 = os.path.join(cls.data_dir, 'modify2.geom')

    def test_modify1_sum(self):
        mock_tk = MagicMock() # глушилка TkDrawer
        polyedr = Polyedr(self.test_file_modify1)
        result_sum = polyedr.draw(mock_tk)
        expected_sum = 4480.0
        self.assertAlmostEqual(result_sum, expected_sum)

    def test_modify2_sum(self):
        mock_tk = MagicMock() # глушилка TkDrawer
        polyedr = Polyedr(self.test_file_modify2)
        result_sum = polyedr.draw(mock_tk)
        expected_sum = 1120.0
        self.assertAlmostEqual(result_sum, expected_sum)


if __name__ == "__main__":
    unittest.main()