#day schedule class
#author Emmanuel Ashimwe 222127212 

from models.task import Task
from dataclasses import dataclass,field
from datetime import date,time
import heapq # will be used to set the heap structure

@dataclass
class DaySchedule: 
    name : str
    dayDate :date
    dateTime : time 
    tasks : list[Task] # will be turned into a heap idk how but i will soon


