#schedule class 
# author : Emmanuel Ashimwe 222127212 

from models.daySchedule import DaySchedule
from dataclasses import dataclass,field
from typing import Dict


@dataclass
class Schedule:
     daySchedules: Dict[str, DaySchedule] = field(default_factory=dict) 

     def getDay(self,day: str):
          return self.daySchedules.get(day)
     
     def addDaySchedule(self, day: str, dayToAdd : DaySchedule):
          self.daySchedules[day] = dayToAdd
     