# SRP: The Single Responsibility Principle

# (2017) A module should be responsible to one, and only one, actor.
# model = class
# actor = who it's responsible to serve

# (2002) A class should have only one reason to change.

# (2000) There should never be more than one reason for
# a class to change.


class TelephoneDirectory:
    def __init__(self):
        self.directory = dict()

    def add_entry(self, name, number):
        self.directory[name] = number

    def retrieve_entry(self, name):
        return self.directory[name]

    def update_entry(self, name, number):
        self.directory[name] = number


class StoreManager:
    def persist_to_s3(self, data):
        pass
