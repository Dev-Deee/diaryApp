from diary.DiaryApp import Diary


class Diaries:
    def __init__(self):
        self.__diaries = []

    def add_diary(self, user_name, pin):
        if self.__exists_by_user_name(user_name):
            raise ValueError("Diary with this username already exists")
        self.__diaries.append(Diary(user_name, pin))

    def find_by_user_name(self, user_name):
        for diary in self.__diaries:
            if diary.get_user_name() == user_name:
                return diary
        raise ValueError("Diary not found")

    def delete(self, user_name):
        for index, diary in enumerate(self.__diaries):
            if diary.get_user_name() == user_name:
                self.__diaries.pop(index)
                return
        raise ValueError("Diary not found")

    def get_diary_count(self):
        return len(self.__diaries)

    def __exists_by_user_name(self, user_name):
        for diary in self.__diaries:
            if diary.get_user_name() == user_name:
                return True
        return False