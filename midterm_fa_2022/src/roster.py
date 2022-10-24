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

    def save_roster(self):
        pass
