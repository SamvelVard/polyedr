import unittest
import os
import sys
from unittest.mock import MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from shadow.polyedr import Polyedr


class TestPolyedr(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data_dir = os.path.join(os.path.dirname(__file__), "..", "data")
        cls.test_file_modify1 = os.path.join(cls.data_dir, "modify1.geom")
        cls.test_file_modify2 = os.path.join(cls.data_dir, "modify2.geom")
        cls.test_file_modify3 = os.path.join(cls.data_dir, "modify3.geom")
        cls.test_file_modify4 = os.path.join(cls.data_dir, "modify4.geom")
        cls.test_file_modify5 = os.path.join(cls.data_dir, "modify5.geom")

    def test_modify1_sum(self):
        mock_tk = MagicMock()  # глушилка TkDrawer
        polyedr = Polyedr(self.test_file_modify1)
        result_sum = polyedr.draw(mock_tk)
        expected_sum = 1120.0
        self.assertAlmostEqual(round(result_sum), expected_sum)

    def test_modify2_sum(self):
        mock_tk = MagicMock()  # глушилка TkDrawer
        polyedr = Polyedr(self.test_file_modify2)
        result_sum = polyedr.draw(mock_tk)
        expected_sum = 280.0
        self.assertAlmostEqual(round(result_sum), expected_sum)

    def test_modify3_sum(self):
        mock_tk = MagicMock()  # глушилка TkDrawer
        polyedr = Polyedr(self.test_file_modify3)
        result_sum = polyedr.draw(mock_tk)
        expected_sum = 1400.0
        self.assertAlmostEqual(round(result_sum), expected_sum)

    def test_modify4_sum(self):
        mock_tk = MagicMock()  # глушилка TkDrawer
        polyedr = Polyedr(self.test_file_modify4)
        result_sum = polyedr.draw(mock_tk)
        expected_sum = 560.0
        self.assertAlmostEqual(round(result_sum), expected_sum)

    def test_modify5_sum(self):
        mock_tk = MagicMock()  # глушилка TkDrawer
        polyedr = Polyedr(self.test_file_modify5)
        result_sum = polyedr.draw(mock_tk)
        expected_sum = 1680.0
        self.assertAlmostEqual(round(result_sum), expected_sum)


if __name__ == "__main__":
    unittest.main()
