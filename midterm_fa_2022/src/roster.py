"""Implements Team Roster Operations"""

"""Imports json so roster can be imported/saved, and date from datetime so date can be added to roster"""
import json
from datetime import date
class Roster(object):
    """Implements Team Roster Operations"""
    def __init__(self):
        #create initial empty roster
        self._create_new_roster()

    def new_roster(self):
        user_input = input("Save current roster? (y/n): ")[0]
        match user_input.lower():
            case 'y':
                self.save_roster()
                self._create_new_roster()
            case 'n':
                self._create_new_roster()
            case _:
                self._create_new_roster()
    
    def _create_new_roster(self):
        self.roster = {}
        self.roster['type'] = 'Team Roster'
        self.roster['date'] = date.today().isoformat()
        self.roster['sport'] = 'Curling'
        self.roster['country'] = 'USA'
        self.roster['members'] = []

    """Retrieve file path of json file"""
    def _retrieve_file_path(self):
        where_file = input("Please enter the path and filename: ")
        return where_file

    def load_roster(self):
        if __debug__:
            print('attempting to load roster...')
        try:
            file_path = self._retrieve_file_path()
            with open(file_path, 'r', encoding='UTF-8') as f:
                self.roster = json.loads(f.read())
        except OSError:
            print('File path or file does not exist. Try again.')
        
    def add_members(self, new_member, member_age):
        if __debug__:
            print('Adding new member to roster.')
        self.roster['members'].append({"name" : new_member, "age" : int(member_age)})

    def save_roster(self):
        pass