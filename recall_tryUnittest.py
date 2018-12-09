
import unittest


class MyCase(unittest.TestCase):

    def setUp(self):
        print("in setUp")

    def tearDown(self):
        print("in tearDown")

    def test_equal(self):
        self.assertEqual("a", "a")

    def test_in(self):
        self.assertIn("百度", "百度一下，你就知道", "不在")

    def test_list(self):
        self.assertListEqual([1, 2, 3], [1, 2, 3], "Not Equal")


if __name__ == "__main__":
    unittest.main()

