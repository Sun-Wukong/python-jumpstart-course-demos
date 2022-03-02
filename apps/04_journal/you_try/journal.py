from collections import deque
from io import FileIO as file
from time import sleep

journal_dir = "data/"


class Journal():
    def __init__(self, journal_name):
        self.name = journal_name
        self.entries = list()
        self.unsaved_entries = deque()
        self.__load__(journal_name)

    def __load__(self, journal_name):
        try:
            with open("{}{}.jrn".format(journal_dir, journal_name), "r") as f:
                for entry in f.readlines():
                    self.entries.append(entry.strip("\n"))
        except FileNotFoundError:
            print("File {}{}.jrn was not found".format(
                journal_dir, journal_name))

    def add_entry(self, entry):
        try:
            if entry is None:
                raise Exception
            else:
                if(isinstance(entry, (int, float))):
                    self.unsaved_entries.append("{}".format(entry))
                else:
                    self.unsaved_entries.append(entry)
        except Exception:
            print("Invalid input")

    def get_entries(self):
        return {
            "entries": self.entries,
            "unsaved": self.unsaved_entries
        }

    def save(self):
        print("saving changes")
        with file.open("{}{}.jrn".format(journal_dir, self.name), "w+") as f:
            for entry in self.unsaved_entries[:2]:
                # TODO: write in retry logic, if desriable
                f.write(b"{},".format(entry))
                print("Saved entry {}".format(
                    self.unsaved_entries.index(entry, 0, -2) + 1))
            f.write(b"{}".format(self.unsaved_entries.pop()))
            print("saved last entry")
            sleep(3000)
