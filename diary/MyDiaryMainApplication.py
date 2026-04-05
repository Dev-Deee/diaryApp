from diary.Diaries import Diaries
1
class MyDiaryMainApplication:
    def __init__(self):
        self.__diaries = Diaries()

    def run(self):
        running = True
        while running:
            self.__print_main_menu()
            choice = self.__read_int("Choose an option: ")

            match choice:
                case 1: self.__create_diary()
                case 2: self.__open_diary()
                case 3: self.__delete_diary()
                case 4: print(f"Total diaries: {self.__diaries.get_diary_count()}")
                case 0:
                    running = False
                    print("Goodbye.")
                case _: print("Invalid option.")

    def __print_main_menu(self):
        print()
        print("=== Diary App ===")
        print("1. Create diary")
        print("2. Open diary")
        print("3. Delete diary")
        print("4. Show diary count")
        print("0. Exit")

    def __create_diary(self):
        user_name = input("Username: ")
        pin = input("4-digit PIN: ")
        try:
            self.__diaries.add_diary(user_name, pin)
            print("Diary created.")
        except ValueError as error:
            print(str(error))

    def __open_diary(self):
        user_name = input("Username: ")
        pin = input("PIN: ")
        try:
            diary = self.__diaries.find_by_user_name(user_name)
            diary.un_lock_diary(pin)
            print("Diary unlocked.")
            self.__diary_session(diary)
        except ValueError as error:
            print(str(error))

    def __delete_diary(self):
        user_name = input("Username to delete: ")
        try:
            self.__diaries.delete(user_name)
            print("Diary deleted.")
        except ValueError as error:
            print(str(error))

    def __diary_session(self, diary):
        active = True
        while active:
            self.__print_diary_menu(diary.get_user_name())
            choice = self.__read_int("Choose an option: ")
            try:
                match choice:
                    case 1: self.__create_entry(diary)
                    case 2: self.__view_entry_by_id(diary)
                    case 3: self.__update_entry(diary)
                    case 4: self.__delete_entry(diary)
                    case 5: self.__change_pin(diary)
                    case 6:
                        diary.lock_diary()
                        active = False
                        print("Diary locked.")
                    case 7: print(f"Entry count: {diary.get_entry_count()}")
                    case _: print("Invalid option.")
            except ValueError as error:
                print(str(error))

    def __print_diary_menu(self, user_name):
        print()
        print(f"=== Diary: {user_name} ===")
        print("1. Create entry")
        print("2. View entry by id")
        print("3. Update entry")
        print("4. Delete entry")
        print("5. Change PIN")
        print("6. Lock and logout")
        print("7. Show entry count")

    def __create_entry(self, diary):
        title = input("Title: ")
        body = input("Body: ")
        diary.create_entry(title, body)
        print("Entry created.")

    def __view_entry_by_id(self, diary):
        entry_id = self.__read_int("Entry id: ")
        entry = diary.find_entry_by_id(entry_id)
        print(f"Id: {entry.get_id()}")
        print(f"Title: {entry.get_title()}")
        print(f"Body: {entry.get_body()}")
        print(f"Created: {entry.get_date_created()}")

    def __update_entry(self, diary):
        entry_id = self.__read_int("Entry id: ")
        title = input("New title: ")
        body = input("New body: ")
        diary.update_entry(entry_id, title, body)
        print("Entry updated.")

    def __delete_entry(self, diary):
        entry_id = self.__read_int("Entry id: ")
        diary.delete_entry(entry_id)
        print("Delete operation complete.")

    def __change_pin(self, diary):
        old_pin = input("Old PIN: ")
        new_pin = input("New 4-digit PIN: ")
        diary.change_pin(old_pin, new_pin)
        print("PIN changed.")

    def __read_int(self, prompt):
        while True:
            raw = input(prompt)
            try:
                return int(raw)
            except ValueError:
                print("Please enter a valid number.")


if __name__ == "__main__":
    MyDiaryMainApplication().run()