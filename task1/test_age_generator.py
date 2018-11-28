from unittest import TestCase, main
from task1.csv_generator import age_generator


class TestAge_generator(TestCase):
    def test_age_generator(self):
        with self.assertRaises(SystemExit) as cm:
            age_generator(-1)
            age_generator(0)
            age_generator(1)

        self.assertEqual(cm.exception.code, 1)
        self.assertEqual(len(age_generator(2)), 2)
        self.assertEqual(len(age_generator(20001)), 20001)
        self.assertEqual(len(age_generator(50000)), 50000)


if __name__ == '__main__':
    main()
