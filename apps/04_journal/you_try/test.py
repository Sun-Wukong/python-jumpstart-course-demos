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

test_ge_items = [
    "Test 1",
    "test 2",
    "12345",
]


def run_evt_loop():
    pass


def test_get_entries(journal_name, test_set):
    journal = Journal(journal_name)
    try:
        assert journal.get_entries()["entries"] == test_set
        print("Test passed")
    except AssertionError:
        print("journal.get_entries failed to produce a match")
    pass


def test_add_entry(journal, test_set):
    unsaved = journal.get_entries()["unsaved"]
    try:
        if(test_set is None):
            assert(test_set not in unsaved)
        elif(type(test_set) == int or float):
            assert str(test_set in unsaved)
            print("Successfully added entry to journal:\n{}".format(test_set))
        else:
            assert(test_set in unsaved)
            print("Successfully added entry to journal:\n{}".format(test_set))
    except AssertionError:
        print("Test input {} failed".format(test_set))


def test_load(journal_name, test_set):
    try:
        test_journal = Journal(journal_name)
        entries = test_journal.get_entries()
        assert_against = [str(item) for item in test_set]
        assert(len(entries) > 0)
        assert(entries == assert_against)
        print("Passed")
    except AssertionError:
        print("Test journal was not loaded properly")
    except FileNotFoundError:
        print("The {}.jrn file was not found".format(journal_name))
    pass


def test_save(journal):
    print("Attempting a save")
    try:
        journal.save()
    except Exception:
        print("Failed to save journal {}".format(journal.name))
    print("Successfully saved {}.jrn".format(journal.name))


if __name__ == '__main__':
    # print("Testing Journal.load")
    # test_load("test")
    # sleep(3)

    print("Testing Journal.get_entries")
    test_get_entries("test", test_ge_items)
    sleep(3)

    print("Testing Journal.add_entry")
    blank_jrn = Journal("blank")
    for item in test_entries:
        blank_jrn.add_entry(item)
        test_add_entry(blank_jrn, item)
    sleep(3)

    print("Testing Journal.save")
    test_save(blank_jrn)
    sleep(3)
