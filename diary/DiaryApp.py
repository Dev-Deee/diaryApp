import re
from datetime import datetime

class Entry:
    def __init__(self, entry_id, title, body):
        if entry_id <= 0:
            raise ValueError("Entry id must be greater than zero")
        self.__validate_text(title, "Title")
        self.__validate_text(body, "Body")
        self.__id = entry_id
        self.__title = title
        self.__body = body
        self.__date_created = datetime.now()

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__validate_text(title, "Title")
        self.__title = title

    def get_body(self):
        return self.__body

    def set_body(self, body):
        self.__validate_text(body, "Body")
        self.__body = body

    def get_date_created(self):
        return self.__date_created

    def __validate_text(self, value, field_name):
        if value is None or value.strip() == "":
            raise ValueError(f"{field_name} cannot be empty")


class Diary:
    def __init__(self, user_name, pin):
        self.__validate_user_name(user_name)
        self.__validate_pin(pin)
        self.__user_name = user_name
        self.__pin = pin
        self.__is_locked = True
        self.__entries = []
        self.__next_entry_id = 1

    def get_user_name(self):
        return self.__user_name

    def get_diary_status(self):
        return self.__is_locked

    def lock_diary(self):
        self.__is_locked = True

    def un_lock_diary(self, pin):
        if pin != self.__pin:
            raise ValueError("Pins don't match")
        self.__is_locked = False

    def change_pin(self, old_pin, new_pin):
        if old_pin != self.__pin:
            raise ValueError("Old pin is incorrect")
        self.__validate_pin(new_pin)
        self.__pin = new_pin

    def create_entry(self, title, body):
        if self.__is_locked:
            raise ValueError("Diary is locked")
        self.__entries.append(Entry(self.__next_entry_id, title, body))
        self.__next_entry_id += 1

    def find_entry_by_id(self, entry_id):
        if self.__is_locked:
            raise ValueError("Diary is locked")
        for entry in self.__entries:
            if entry.get_id() == entry_id:
                return entry
        raise ValueError("Entry not found")

    def update_entry(self, entry_id, title, body):
        if self.__is_locked:
            raise ValueError("Diary is locked")
        for entry in self.__entries:
            if entry.get_id() == entry_id:
                entry.set_title(title)
                entry.set_body(body)
                return
        raise ValueError("Entry not found")

    def delete_entry(self, entry_id):
        if self.__is_locked:
            raise ValueError("Diary is locked")
        for index, entry in enumerate(self.__entries):
            if entry.get_id() == entry_id:
                self.__entries.pop(index)
                return
        raise ValueError("Entry not found")

    def get_entry_count(self):
        return len(self.__entries)

    def __validate_pin(self, pin):
        if pin is None or not re.fullmatch(r'\d{4}', pin):
            raise ValueError("Pin must be exactly 4 digits")

    def __validate_user_name(self, user_name):
        if user_name is None or user_name.strip() == "":
            raise ValueError("Username cannot be empty")
