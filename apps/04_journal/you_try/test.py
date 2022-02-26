import unittest
from time import sleep
from journal import Journal

# Mock data and functions(if needed)
test_entries = [
    "Test 1",
    "test 2",
    12345,
    None
]

def run_evt_loop():
    pass


def test_get_entries(journal_name, test_set):
    #TODO: Create cases for empty journal and filled journal
    journal = Journal(journal_name)
    if len(journal.entries == 0):
        journal.entries = test_set
    try:
        assert journal.get_entries() == test_set
    except AssertionError:
        print("journal.get_entries failed to produce a match")
    pass


def test_add_entry(journal, test_set):
    journal.add_entry(test_set)
    try:
        assert(test_set in journal.entries == True)
    except AssertionError:
        print("Entry {}\n was not added".format(test_set)) 


def test_load(journal_name):
    try:
        test_journal = Journal(journal_name)
    except FileNotFoundError:
        print("The {}.jrn file was not found".format(journal_name))
    pass


def save():
    pass

if __name__ == '__main__':
    print("Testing Journal.load")
    test_load("test")
    sleep(3)
    # print("Testing Journal.add_entry")
    # sleep(3)
    # print("Testing Journal.get_entries")
    # sleep(3)
    # print("Testing Journal.save")
    # pass