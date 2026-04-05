import unittest
from diary.Diaries import Diaries

class DiariesTest(unittest.TestCase):

    def setUp(self):
        self.diaries = Diaries()

    def test_that_diary_can_be_added(self):
        self.diaries.add_diary("arike", "0123")
        self.assertEqual(1, self.diaries.get_diary_count())

    def test_that_duplicate_user_name_throws_exception(self):
        self.diaries.add_diary("arike", "0123")
        with self.assertRaises(ValueError):
            self.diaries.add_diary("arike", "1111")

    def test_that_diary_can_be_found_by_user_name(self):
        self.diaries.add_diary("arike", "0123")
        found = self.diaries.find_by_user_name("arike")
        self.assertEqual("arike", found.get_user_name())

    def test_that_finding_unknown_diary_throws_exception(self):
        with self.assertRaises(ValueError):
            self.diaries.find_by_user_name("unknown")

    def test_that_diary_can_be_deleted(self):
        self.diaries.add_diary("arike", "0123")
        self.diaries.delete("arike")
        self.assertEqual(0, self.diaries.get_diary_count())

    def test_that_deleting_unknown_diary_throws_exception(self):
        with self.assertRaises(ValueError):
            self.diaries.delete("unknown")

if __name__ == "__main__":
    unittest.main()