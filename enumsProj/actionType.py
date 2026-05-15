# action type class
# Author : Emmanuel Ashimwe 
from enum import Enum

class ActionType(Enum):
    PRIORITIZE : str = 'PRIORITIZE'
    NO_ACTION : str = 'NO_ACTION'
    UPDATE_TASK : str = 'UPDATE_TASK'
    ADD_URGENT : str = 'ADD_URGENT'
    RESCHDEULE: str  = 'RESCHDEULE'
    SCHEDULE : str = 'SCHEDULE' 
    SUGGEST_OPTIMAL : str = 'SUGGEST_OPTIMAL'

    