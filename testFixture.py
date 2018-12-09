import unittest


class MyFirstFixture(unittest.TestCase):
    mylst = [1,2,3]

    def setUp(self):
        self.mylst = [1, 2, 3]
        print("SSSSSSSSSSSSSSSSSSSSSSS")

    def test_case_1(self):
        self.assertEqual("a", "a", "they are not equal.")  # assert 断言
        print("1111111111111111")

    def test_case_num(self):
        self.assertEqual("a", "a", "they are not equal.")  # assert 断言
        print("nnnnnn")

    def test_case_list(self):
        self.assertListEqual([1,2,3], self.mylst, "they are not equal.")
        print("LLLLLL")

    def tearDown(self):
        self.mylst = None
        print("tttttttttttttttttttt")


if __name__ == "__main__":
    unittest.main()

