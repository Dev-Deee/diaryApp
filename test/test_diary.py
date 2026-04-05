import unittest
from diary.diary import Diary

class DiaryTest(unittest.TestCase):

    def setUp(self):
        self.diary = Diary("Arike OmoOba", "0123")

    def test_that_diary_is_locked_by_default(self):
        self.assertTrue(self.diary.get_diary_status())

    def test_that_diary_can_be_unlocked_with_the_correct_password(self):
        self.assertTrue(self.diary.get_diary_status())
        self.diary.un_lock_diary("0123")
        self.assertFalse(self.diary.get_diary_status())

    def test_that_incorrect_password_throws_exception(self):
        with self.assertRaises(ValueError):
            self.diary.un_lock_diary("wrongpassword")

    def test_that_entry_can_be_created(self):
        self.diary.un_lock_diary("0123")
        self.diary.create_entry("Day 1", "Today was a good day.")
        self.assertEqual(1, self.diary.get_entry_count())

    def test_that_multiple_entries_can_be_created(self):
        self.diary.un_lock_diary("0123")
        self.diary.create_entry("Day 1", "Today was a good day.")
        self.diary.create_entry("Day 2", "Today was even better.")
        self.assertEqual(2, self.diary.get_entry_count())

    def test_that_creating_entry_when_locked_throws_exception(self):
        with self.assertRaises(ValueError):
            self.diary.create_entry("Day 1", "Today was a good day.")

    def test_that_entry_title_can_be_updated(self):
        self.diary.un_lock_diary("0123")
        self.diary.create_entry("Day 1", "Today was a good day.")
        self.diary.update_entry(1, "Day 1 Updated", "Today was a good day.")
        self.assertEqual("Day 1 Updated", self.diary.find_entry_by_id(1).get_title())

    def test_that_entry_body_can_be_updated(self):
        self.diary.un_lock_diary("0123")
        self.diary.create_entry("Day 1", "Today was a good day.")
        self.diary.update_entry(1, "Day 1", "Today was great.")
        self.assertEqual("Today was great.", self.diary.find_entry_by_id(1).get_body())

    def test_that_updating_entry_when_locked_throws_exception(self):
        self.diary.un_lock_diary("0123")
        self.diary.create_entry("Day 1", "Today was a good day.")
        self.diary.lock_diary()
        with self.assertRaises(ValueError):
            self.diary.update_entry(1, "Day 1 Updated", "Today was great.")

    def test_that_updating_invalid_entry_throws_exception(self):
        self.diary.un_lock_diary("0123")
        with self.assertRaises(ValueError):
            self.diary.update_entry(99, "Day 1 Updated", "Today was great.")

    def test_that_finding_entry_when_locked_throws_exception(self):
        with self.assertRaises(ValueError):
            self.diary.find_entry_by_id(1)

    def test_that_finding_invalid_entry_throws_exception(self):
        self.diary.un_lock_diary("0123")
        with self.assertRaises(ValueError):
            self.diary.find_entry_by_id(999)

    def test_that_entry_can_be_deleted(self):
        self.diary.un_lock_diary("0123")
        self.diary.create_entry("Day 1", "Today was a good day.")
        self.diary.delete_entry(1)
        self.assertEqual(0, self.diary.get_entry_count())

    def test_that_deleting_entry_when_locked_throws_exception(self):
        self.diary.un_lock_diary("0123")
        self.diary.create_entry("Day 1", "Today was a good day.")
        self.diary.lock_diary()
        with self.assertRaises(ValueError):
            self.diary.delete_entry(1)

    # def test_that_deleting_invalid_entry_does_not_change_count(self):
    #     self.diary.un_lock_diary("0123")
    #     self.diary.create_entry("Day 1", "Today was a good day.")
    #     self.diary.delete_entry(99)
    #     self.assertEqual(1, self.diary.get_entry_count())

    def test_that_entry_ids_are_not_reused_after_delete(self):
        self.diary.un_lock_diary("0123")
        self.diary.create_entry("Day 1", "Today was a good day.")
        self.diary.create_entry("Day 2", "Today was even better.")
        self.diary.delete_entry(1)
        self.diary.create_entry("Day 3", "Today was best.")
        self.assertEqual(3, self.diary.find_entry_by_id(3).get_id())

    def test_that_diary_with_invalid_pin_throws_exception(self):
        with self.assertRaises(ValueError):
            Diary("Arike OmoOba", "12")
        with self.assertRaises(ValueError):
            Diary("Arike OmoOba", "abcd")

    def test_that_pin_can_be_changed_with_correct_old_pin(self):
        self.diary.change_pin("0123", "1111")
        with self.assertRaises(ValueError):
            self.diary.un_lock_diary("0123")
        self.diary.un_lock_diary("1111")
        self.assertFalse(self.diary.get_diary_status())

    def test_that_changing_pin_with_wrong_old_pin_throws_exception(self):
        with self.assertRaises(ValueError):
            self.diary.change_pin("9999", "1111")

    def test_that_changing_pin_with_invalid_new_pin_throws_exception(self):
        with self.assertRaises(ValueError):
            self.diary.change_pin("0123", "11")

    def test_that_diary_with_invalid_user_name_throws_exception(self):
        with self.assertRaises(ValueError):
            Diary(" ", "0123")


if __name__ == "__main__":
    unittest.main()