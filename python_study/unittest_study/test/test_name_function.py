import unittest
from unittest_study.name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    """
    测试 get_formatted_name
    """
    def test_first_last_name(self):
        """
        test get_formatted_name
        :return:
        """
        formatted_name = get_formatted_name("gou", "liyang")
        self.assertEqual(formatted_name, "Gou Liyang")


if __name__ == "__main":
    unittest.main()