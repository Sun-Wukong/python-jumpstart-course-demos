from sys import argv
from time import sleep
from journal import Journal


def cmd(key, journal):
    if (key == "l".lower() or key == "L"):
        index = 1
        print("Your journal entries:\n")
        for entry in journal.entries:
            print("{}. {}".format(index, entry))
            index += 1
    elif (key == "a".lower() or key == "A"):
        index = 1
        print("Write your new entry. Press \'return\' to save")
        new_entry = input()
        journal.add_entry(new_entry)
        print("Unsaved entries:\n")
        for unsaved in list(journal.unsaved_entries):
            print("{}. {}".format(index, unsaved))
            index += 1
    elif (key == "x" or key == "X"):
        print("Saving before exit")
        print("... saving to ./data/{}.jrn".format(journal.name))
        journal.save()
        sleep(4)
        print("... save complete ...")
        exit(0)
    else:
        print("{} is not a command".format(key))


def run_evt_loop(journal):
    while True:
        print("\nWhat do you want to do? [L]ist, [A]dd, or E[x]it? ")
        cmd(input(), journal)
    # pass


header = [
    "---------------------------------",
    "      PERSONAL JOURNAL APP",
    "---------------------------------"
]


if __name__ == "__main__":
    for line in header:
        print(line)
    print("... loading journal from ./data/{}.jrn ...".format(argv[0]))
    my_jrn = Journal(argv[1])
    print("... loaded {} entries ...".format(len(my_jrn.entries)))
    run_evt_loop(my_jrn)
