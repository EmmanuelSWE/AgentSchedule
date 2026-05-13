#schedule class 
# author : Emmanuel Ashimwe 222127212 

from models.daySchedule import DaySchedule
from dataclasses import dataclass,field
from typing import TypedDict

class DayDict: # dictionary object of days so its is easier to retirieve
    date : str
    scheduleObject : DaySchedule

@dataclass
class Schedule:
    daySchedules : DayDict