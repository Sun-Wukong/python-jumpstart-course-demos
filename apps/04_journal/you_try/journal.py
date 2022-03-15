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
        # def newliner(x): return "{}\n".format(x)
        if(len(self.unsaved_entries) == 0):
            print("No entries to save")
        elif(len(self.unsaved_entries) == 1):
            self.entries.append(self.unsaved_entries.pop())
            print("saving changes")
            with open("{}{}.jrn".format(journal_dir, self.name), "w+") as f:
                f.write(self.entries)
            print("Entries saved: {}".format(self.entries))
        else:
            # last_entry = self.unsaved_entries.pop()
            print("saving changes")
            with open("{}{}.jrn".format(journal_dir, self.name), "w+") as f:
                while(len(self.unsaved_entries) > 0):
                    self.entries.append(self.unsaved_entries.popleft())
                # self.entries.append(last_entry)
                stringified_entries = "".join(
                    ["{}\n".format(n) for n in self.entries])
                f.write(stringified_entries)
                print("Entries saved:\n{}".format(stringified_entries))
