from unittest import TestCase, main
from task1.csv_generator import name_generator


class TestName_generator(TestCase):
    def test_name_generator(self):
        with self.assertRaises(SystemExit) as cm:
            name_generator(1)
            name_generator(-1)
            name_generator(20001)

        self.assertEqual(cm.exception.code, 1)
        self.assertEqual(len(name_generator(2)), 2)
        self.assertEqual(len(name_generator(20000)), 20000)


if __name__ == '__main__':
    main()
